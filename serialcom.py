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
    arduinoData = (serial.readline())
    if (arduinoData == 3):
        theftAlert = True
        print('t')
    elif (arduinoData == 2):
        suspiciousActivity = True
        print('s')
    
