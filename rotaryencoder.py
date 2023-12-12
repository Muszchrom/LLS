from machine import Pin

# basic python implementation of
# https://github.com/mo-thunderz/RotaryEncoder/blob/main/Arduino/ArduinoRotaryEncoder/ArduinoRotaryEncoder.ino
class RotaryEncoder:
    def __init__(self, clk, dt):
        self._IRQ_BOTH_EDGES = Pin.IRQ_FALLING | Pin.IRQ_RISING
        self._ENC_STATES = [0,-1,1,0,1,0,0,-1,-1,0,0,1,0,1,-1,0]
        
        self.human_counter = 0
        self.enc_state = 0x03
        self.counter = 0
        
        self.clk_pin = Pin(clk, Pin.IN, Pin.PULL_UP)
        self.dt_pin = Pin(dt, Pin.IN, Pin.PULL_UP)
        
        self.clk_pin.irq(self._interrupt_handler, self._IRQ_BOTH_EDGES) # Run handler on both edges
        self.dt_pin.irq(self._interrupt_handler, self._IRQ_BOTH_EDGES)
        
    def _interrupt_handler(self, _):
        self.enc_state = self.enc_state << 2
        
        if self.dt_pin.value():
            self.enc_state = self.enc_state | 0x02
        if self.clk_pin.value():
            self.enc_state = self.enc_state | 0x01
        
        self.counter = self.counter + self._ENC_STATES[self.enc_state & 0x0f]
        
        if self.counter > 3:
            self.human_counter = self.human_counter + 1
            self.counter = 0
        elif self.counter < -3:
            self.human_counter = self.human_counter - 1
            self.counter = 0

    def get_value(self):
        return self.human_counter
    
    
