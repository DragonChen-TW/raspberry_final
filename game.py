import RPi.GPIO as gpio
from threading import Thread

from matrix import LEDMatrix

if __name__ == '__main__':
    try:
        matrix = LEDMatrix()

        matrix.startPrint()
        print('a')

        # btn
        gpio.setmode(gpio.BCM)

        print('c')

        btn_gpio = 21
        gpio.setup(btn_gpio, gpio.IN)

        print('start while')
        while True:
            print(gpio.input(btn_gpio))

            if not gpio.input(btn_gpio):
                print('press')
                matrix.now_layer += 1

            time.sleep(2)
    finally:
        gpio.cleanup()
