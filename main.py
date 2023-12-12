from rotaryencoder import RotaryEncoder
from servo import Servo

enc = RotaryEncoder(0, 1)
old_value = enc.get_value()

servo = Servo(13)

angle = 0

while True:
    new_value = enc.get_value()
    if old_value == new_value:
        continue
    
    if new_value < old_value and angle > 0:
        angle -= 5
    elif new_value > old_value and angle < 180:
        angle += 5
    
    old_value = new_value
    servo.set_angle(angle)
        
