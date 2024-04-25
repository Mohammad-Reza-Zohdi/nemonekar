import serial
import time

def send_file_via_serial(port, baudrate, filename):
    try:
        with serial.Serial(port, baudrate, timeout=1) as ser:
            with open(filename, 'rb') as file:
                print(f"Sending data to {port}...")
                while True:
                    data = file.read(1024)
                    if not data:
                        break
                    ser.write(data)
                print("File sent successfully!")
    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    PORT = 'COM1'
    BAUDRATE = 9600
    FILENAME = 'file_to_send.txt'
    
    send_file_via_serial(PORT, BAUDRATE, FILENAME)
