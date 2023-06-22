import serial
import time

# Replace with the appropriate serial port and baud rate
serial_port = 'COM3'
baud_rate = 9600

# Open the serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=1)
while(True):

# Wait for the Arduino to reset
    time.sleep(2)

# Send commands to the Arduino to turn the LED on and off
    ser.write(b'1')  # Send '1' to turn the LED on
    time.sleep(2)
    ser.write(b'0')  # Send '0' to turn the LED off

    status = ser.readline().decode().strip()
    if status == 'True':
        print('Bulb is ON')
    else:
        print('Bulb is OFF')    

