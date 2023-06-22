import cv2
import numpy as np
import tensorflow as tf
import serial
import time

ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the appropriate serial port
ser.timeout = 1

Start = False
IsCapture = False

# Initialize the camera
cap = cv2.VideoCapture(0)

# Load the model
model = tf.keras.models.load_model('RUBBER_seed_classifier.h5')

last_capture_time = time.time()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is captured successfully
    if not ret:
        continue
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    img = cv2.resize(frame, (224, 224))  # Resize the frame to match the input size of the model
    x = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    x = np.expand_dims(x, axis=0)

    # Predict the class label of the captured image using the loaded model
    if IsCapture:
        current_time = time.time()
        if current_time - last_capture_time >= 2:
            preds = model.predict(x)
            threshold = 0.5
            if preds[0][0] < threshold:
                print('Your chosen seed is BAD SEED')
                Start = False
                ser.write(b'1')
                time.sleep(0.5)
                
            else:
                print('Your chosen seed is GOOD SEED')
                Start = True
                ser.write(b'0')
                time.sleep(0.5)
                

                   
            
            last_capture_time = current_time
         

    # Read the value of IsCapture
    ser.write(b'read')  # Send a command to the Arduino to request the value
    response = ser.readline().decode().strip()  # Read the response from the Arduino

    # Set IsCapture based on the response
    if response == '1':
        IsCapture = True
    else:
        IsCapture = False
    
    # Print the value of IsCapture
    print(IsCapture)
    
    if Start == False:
        print("GreenLight")
        ser.write(b'1')
        
        
    else:
        print("RedLight")
        ser.write(b'0')
        
    time.sleep(0.45)    

    # Check for the 'q' key to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()

