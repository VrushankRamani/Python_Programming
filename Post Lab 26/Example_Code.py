import serial as s
import time
arduino = s.Serial(port='COM5', baudrate=9600, timeout=1)
time.sleep(2)

def send_command(command):
  arduino.write(command.encode())
  print(f"Sent: {command}")
  
while True:
    
     user_input = input("Enter '1' to turn ON LED, '0' to turn OFF, 'q' to quit: ")
     if user_input in ['1', '0']:
         send_command(user_input)
     elif user_input == 'q':
       print("Exiting...")
       break
     else:
       print("Invalid input! Enter '1', '0', or 'q'.")
