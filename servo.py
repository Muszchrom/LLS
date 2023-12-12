from machine import PWM

"""
My servo is somewhat weird because angles had to be calculated in unusual way
for 50 Hz and 65535 as max duty value
0.5ms: 0 deg    65535/(20/0.5) = 1639
1.5ms: 90 deg   65535/(20/1.5) = 4915
2.5ms: 180 deg  65535/(20/2.5) = 8191
"""

class Servo:
    def __init__(self, pin, freq=50, min_imp_width=1639, max_imp_width=8191):
        self._servo = PWM(pin, freq=freq)
        self.min_imp_width=min_imp_width
        self.max_imp_width=max_imp_width
        
    def set_angle(self, deg):
        if deg < 0:
            deg = 0
        elif deg > 180:
            deg = 180
        new_pos = int(self.min_imp_width + deg/180*(self.max_imp_width - self.min_imp_width))
        self._servo.duty_u16(new_pos)
