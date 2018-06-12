import RPi.GPIO as gpio
import time

class Register:
    def __init__(self, DS, SHCP, STCP):
        self.DS = DS
        self.SHCP = SHCP
        self.STCP = STCP

    def shift(self, i, shift_data):
        gpio.output(self.STCP[i], gpio.LOW)
        for d in shift_data:
            gpio.output(self.SHCP[i], gpio.LOW)
            gpio.output(self.DS[i], int(d))
            gpio.output(self.SHCP[i], gpio.HIGH)
        gpio.output(self.STCP[i], gpio.HIGH)
