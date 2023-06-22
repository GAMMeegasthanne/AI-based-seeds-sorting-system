import cv2
import numpy as np
import tensorflow as tf
import serial

# Configure the serial connection
arduino = serial.Serial('COM4', 9600)  # Replace 'COM4' with the appropriate serial port
arduino.timeout = 1

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # Wait for user input to capture the image
    key = cv2.waitKey(1)
    if key == ord('s'):
        # Save the captured image
        cv2.imwrite('captured_image.jpg', frame)
    
    line = arduino.readline().decode().strip()
    if line:
        bulbOn = bool(int(line))
        if bulbOn:
            print("Bulb is ON")
        else:
            print("Bulb is OFF")
            cv2.imwrite('captured_image.jpg', frame)
            
            # Load the captured image and preprocess it for prediction
            img_path = 'captured_image.jpg'
            img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
            x = tf.keras.preprocessing.image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = tf.keras.applications.mobilenet_v2.preprocess_input(x)
            model = tf.keras.models.load_model('RUBBER_seed_classifier.h5')

            # Predict the class label of the captured image using the loaded model
            preds = model.predict(x)
            threshold = 0.5
            if preds[0][0] < threshold:
                print('Your chosen seed is BAD SEED')
            else:
                print('Your chosen seed is GOOD SEED')
    
    # Exit the loop if 'q' is pressed
    if key == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
