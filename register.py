import RPi.GPIO as gpio

class Register:
    def __init__(self, DS, SHCP, STCP):
        self.DS = DS
        self.SHCP = SHCP
        self.STCP = STCP

        gpio.setmode(gpio.BCM)
        for g in self.DS + self.SHCP + self.STCP:
            gpio.setup(g, gpio.OUT)

    def makeTick(self, gpio_num):
        gpio.output(gpio_num, gpio.HIGH)
        gpio.output(gpio_num, gpio.LOW)

    def shift(self, i, shift_data):
        for d in shift_data:
            gpio.output(self.DS[i], int(d))
            self.makeTick(self.SHCP[i])
        self.makeTick(self.STCP[i])
