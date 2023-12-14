from servo import Servo
from machine import UART

servo_v = Servo(13)
servo_h = Servo(12)
uart = UART(0, 115200)

x=0
y=0
while True:
    if uart.any():
        data = uart.readline()
        if len(data) != 2:
            continue
        x, y = data
        
    servo_h.set_angle(x)
    servo_v.set_angle(y)

