import RPi.GPIO as gpio
import time
from threading import Thread

from matrix import LEDMatrix

if __name__ == '__main__':
    try:
        matrix = LEDMatrix(100)

        matrix.startPrint()

        gpio.setmode(gpio.BCM)
        btn_gpio = 21
        gpio.setup(btn_gpio, gpio.IN)

        while True:
            if not gpio.input(btn_gpio):
                time.sleep(0.01)
                while not gpio.input(btn_gpio):
                    time.sleep(0.01)

                print('press')
                matrix.now_layer += 1

            time.sleep(0.01)
    finally:
        gpio.cleanup()
