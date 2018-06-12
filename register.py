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

        gpio.output(STCP, gpio.LOW)
        for d in range(8):
            gpio.output(self.SHCP[i], gpio.LOW)
            gpio.output(self.DS[i], 0)
            gpio.output(self.SHCP[i], gpio.HIGH)
        gpio.output(STCP, gpio.HIGH)

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


        register.shift(0, '11111111')

        temp = [
            '01111111',
            '10111111',
            '11011111',
            '11101111',
            '11110111',
            '11111011',
            '11111101',
            '11111110',
        ]
        for i in range(8):
            register.shift(1, temp[i])
            time.sleep(0.05)
            register.shift(1, '11111111')
        # register.shift(1, '00000000')
        # time.sleep(0.1)
        # register.shift(1, '11111111')

        time.sleep(5)
    finally:
        gpio.cleanup()
