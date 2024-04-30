import serial
import time

class RS232Client:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate

    def is_noise(self, character):
        if not character.isalnum():
            return True
        else:
            return False

    def send_file(self, filename):
        try:
            with serial.Serial(port=self.port, baudrate=self.baudrate, timeout=1) as ser:
                with open(filename, 'rb') as file:
                    print(f"Sending data to {self.port}...")
                    while True:
                        data = file.read(1024)
                        if not data:
                            break
                        for character in data:
                            if self.is_noise(chr(character)):
                                print(f"Noise detected: {chr(character)}")
                                ser.write(b'Resend')  # Ask client to resend
                            else:
                                ser.write(bytes([character]))  # Send valid character
                    print("File sent successfully!")
        except serial.serialutil.SerialException as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    PORT = 'COM3'
    BAUDRATE = 9600
    FILENAME = 'file_to_send.txt'
    
    client = RS232Client(PORT, BAUDRATE)
    client.send_file(FILENAME)
