import serial
import time

# setup
serialPort = '/dev/cu.usbserial-14210'
baudRate = 9600
serial = serial.Serial(serialPort, baudRate, timeout=1)
deviceStatus = 1

def turnOff():
    global deviceStatus
    deviceStatus = 0

def turnOn():
    global deviceStatus
    deviceStatus = 1

turnOn()

# serial comms
while True:
    serial.write((deviceStatus).to_bytes(1, byteorder='big'))
    arduinoData = serial.read()

    if (arduinoData == b'3'):
        # theft alert
        print('t')
    elif (arduinoData == b'2'):
        # suspicious activity
        print('s')
