from machine import Pin
import utime

class Test:
    
    def __init__(self):
        self.LED = Pin(2, Pin.OUT)
        self.LED.value(1)
        self.sleep_time_ms = 2000
        self.start_time = utime.ticks_ms()
        while True:
            if utime.ticks_ms() >= self.start_time + self.sleep_time_ms:
                self.LED.value(not self.LED.value())
                self.start_time = utime.ticks_ms()
                
        
    def check_time(self):
        if utime.ticks_ms() < self.start_time:
            self.start_time = 0
            return False
        return utime.ticks_ms() > (self.start_time + self.sleep_time_ms)
    
    
    def blink(self):
        self.LED.value(not self.LED.value())
        self.start_time = utime.ticks_ms()
    

    def run(self):
        if self.check_time():
            self.blink()
        
