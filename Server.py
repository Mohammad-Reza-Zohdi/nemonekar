import serial
import time

def receive_file_from_serial(port, baudrate, filename):
    try:
        with serial.Serial(port, baudrate, timeout=1) as ser:
            with open(filename, 'wb') as file:
                print(f"Listening for incoming data on {port}...")
                while True:
                    data = ser.read(1024)
                    if not data:
                        break
                    file.write(data)
                print("File received successfully!")
    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    PORT = 'COM1'
    BAUDRATE = 9600
    FILENAME = 'received_file.txt'
    
    receive_file_from_serial(PORT, BAUDRATE, FILENAME)