import RPi.GPIO as gpio
import time
from threading import Thread

from matrix import LEDMatrix

if __name__ == '__main__':
    try:
        matrix = LEDMatrix(100)

        matrix.startPrint()
        print('a')

        # btn
        gpio.setmode(gpio.BCM)

        print('c')

        btn_gpio = 21
        gpio.setup(btn_gpio, gpio.IN)

        print('start while')
        while True:
            if not gpio.input(btn_gpio):
                print('press')
                matrix.now_layer += 1

                while not gpio.input(btn_gpio):
                    time.sleep(0.1)

            time.sleep(0.5)
    finally:
        gpio.cleanup()
