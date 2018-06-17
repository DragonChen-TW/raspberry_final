import RPi.GPIO as gpio
import time
from threading import Thread

from matrix import LEDMatrix


def comparelayer(btn_map):
    #print(matrix.maps[matrix.now_layer])
    if btn_map == matrix.maps[matrix.now_layer]:
        matrix.now_layer += 1

if __name__ == '__main__':
    try:
        matrix = LEDMatrix(100)

        matrix.startPrint()

        gpio.setmode(gpio.BCM)
        btn_gpio_0001 = 21
        btn_gpio_0010 = 16
        btn_gpio_0100 = 5
        btn_gpio_1000 = 23
        gpio.setup(btn_gpio_0001, gpio.IN)
        gpio.setup(btn_gpio_0010, gpio.IN)
        gpio.setup(btn_gpio_0100, gpio.IN)
        gpio.setup(btn_gpio_1000, gpio.IN)

        while True:
            if not gpio.input(btn_gpio_0001):
                while not gpio.input(btn_gpio_0001):
                    time.sleep(0.1)
                # print('press')
                print('btn_gpio_0001')
                comparelayer('0001')
            elif not gpio.input(btn_gpio_0010):
                while not gpio.input(btn_gpio_0010):
                    time.sleep(0.1)
                print('btn_gpio_0010')
                comparelayer('0010')
            elif not gpio.input(btn_gpio_0100):
                while not gpio.input(btn_gpio_0100):
                    time.sleep(0.1)
                print('btn_gpio_0100')
                comparelayer('0100')
            elif not gpio.input(btn_gpio_1000):
                while not gpio.input(btn_gpio_1000):
                    time.sleep(0.1)
                print('btn_gpio_1000')
                comparelayer('1000')

            time.sleep(0.1)
    finally:
        gpio.cleanup()
