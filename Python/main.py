from serial import Serial
import time

def on_message_recived(message: str):
    print(message)



baudrate = 9600
port = 'COM4'

ser = Serial(port, baudrate = baudrate)


time.sleep(0.1)
ser.write(b"server<|M|>Hello, Arduino<|EOM|>")
time.sleep(0.1)
ser.write(b"server<|M|>Hello, Arduino<|EOM|>")
time.sleep(0.1)
ser.write(b"server<|M|>Hello, Arduino<|EOM|>")
time.sleep(0.1)
ser.write(b"server<|M|>Hello, Arduino<|EOM|>")

while(True):
    recived = ser.readline()

    message = recived.decode()

    if message.find("<|EOM|>") > -1:
        ser.write(b"server<|M|><|ACK|>")
        on_message_recived(message)

ser.close()