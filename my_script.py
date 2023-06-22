import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import numpy as np
import tensorflow as tf
from PIL import ImageTk, Image
import serial
import time

# Establish communication with Arduino
arduino = serial.Serial('COM6', 9600)  # Replace 'COM3' with the appropriate port name

def Motor():
    arduino.write(b'1') 
    time.sleep(1.1)
    arduino.write(b'0') 
    
def update_image():
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to an image and display it in the GUI
    if ret:
        image = PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        photo = PIL.ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

    # Schedule the function to be called again after 10 milliseconds
    root.after(10, update_image)

def capture_image():
    # Capture an image from the camera
    ret, frame = cap.read()

    # Hide the camera image label and the capture button
    image_label.pack_forget()
    capture_button.pack_forget()

    # Save the captured image
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
        message_label.config(text='Your chosen seed is BAD SEED')
        arduino.write(b'0')  # Switch off the LED
       

    else:
        message_label.config(text='Your chosen seed is GOOD SEED')
        arduino.write(b'1')  # Switch on the LED
        
    # Display the captured image
    image = PIL.Image.open('captured_image.jpg')
    photo = PIL.ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

def reset():
    # Remove the captured image label and message label
    image_label.pack_forget()
    message_label.config(text="")
    arduino.write(b'0')
    
    # Display the camera image label and the capture button
    capture_button.pack()
    image_label.pack()

root = tk.Tk()
root.title("Camera App")
Motor()
# Set window size to 1280x720 (720p)
root.geometry('1280x720')

# Camera capture
cap = cv2.VideoCapture(0)

# Create a label for the camera image
image_label = tk.Label(root)
image_label.pack()

# Create a button to capture an image from the camera
capture_button = tk.Button(root, text="Capture", command=capture_image)
capture_button.pack()

# Create a button to reset the GUI
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack()

# Create a label for messages
message_label = tk.Label(root, text="")
message_label.pack()

root.after(0, update_image)

root.mainloop()

# Release the camera
cap.release()
cv2.destroyAllWindows()


