import serial
import time

# Configure the serial connection
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the appropriate serial port
ser.timeout = 1

while True:

    ser.write(b'0')
    time.sleep(1)
    ser.write(b'1')
    time.sleep(1)

    line = ser.readline().decode().strip()
    if line:
        bulbOn = bool(int(line))
        if bulbOn:
            print("Bulb is ON")
        else:
            print("Bulb is OFF")