import time
import random
import serial
ser = serial.Serial(
  port='/dev/ttyS0',
  baudrate = 115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

def test_xy(a, b):
    if a < 0:
        a = 0
    elif a > 180:
        a = 180
    if b < 0:
        b = 0
    elif b > 180:
        b = 180
    return [a, b]
            

x=0
y=0
while True:
    opt = input("Type X or Y: ")
    if opt.lower() == "x":
        try:
            x = int(input("angle X: "))
        except ValueError:
            continue
    elif opt.lower() == "y":
        try:
            y = int(input("angle Y: "))
        except ValueError:
            continue
    else:
        continue
    
    x, y = test_xy(x, y)
    print([x, y])
    ser.write([x, y])
    
    
