import RPi.GPIO as gpio
from threading import Thread

from matrix import LEDMatrix

if __name__ == '__main__':
    matrix = LEDMatrix()

    th = Thread(matrix.startPrint())
    th.start()

    # btn
    gpio.setmode(gpio.BCM)
    LED.setup(12, 'in')

    while True:
        if not gpio.input(12):
            print('press')
            matrix.now_layer += 1

        time.sleep(0.5)
