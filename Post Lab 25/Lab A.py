import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)  

def send_message(message):
    # Send message to Arduino
    arduino.write(message.encode('utf-8'))
    print("Sent: {message}")

    # Read response from Arduino
    response = arduino.readline().decode('utf-8').strip()
    if response:
        print("Received: {response}")

while True:
    msg = input("Enter a message to send to Arduino: ")
    send_message(msg)