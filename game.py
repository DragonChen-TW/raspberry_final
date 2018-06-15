import RPi.GPIO as gpio
from threading import Thread

from matrix import LEDMatrix

if __name__ == '__main__':
    matrix = LEDMatrix()

    th = Thread(matrix.startPrint())
    th.start()

    # btn
    gpio.setmode(gpio.BCM)

    btn_gpio = 21
    gpio.setup(btn_gpio, gpio.IN)

    while True:
        if not gpio.input(btn_gpio):
            print('press')
            matrix.now_layer += 1

        time.sleep(0.5)
