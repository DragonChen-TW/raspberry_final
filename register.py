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

if __name__ == '__main__':
    try:
        DS =    [17, 13]
        SHCP =  [22, 26]
        STCP =  [27, 19]

        gpio.setmode(gpio.BCM)
        for g in DS + SHCP + STCP:
            gpio.setup(g, gpio.OUT)

        register = Register(DS, SHCP, STCP)

        # register.shift(1, '00000000')
        # time.sleep(10)

        temp = [
            '10000000',
            '01000000',
            '00100000',
            '00010000',
            '00001000',
            '00000100',
            '00000010',
            '00000001',
        ]
        register.shift(0, '11111111')
        register.shift(1, '11111110')
        time.sleep(0.001)
        register.shift(1, '11111111')
    finally:
        gpio.cleanup()
