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
        btn_gpio = {
            "0001":12,
            "0010":16,
            "0100":20,
            "1000":21
        }
        for key in btn_gpio:
            gpio.setup(btn_gpio[key], gpio.IN)
        gpio.setup(5, gpio.OUT)
        gpio.output(5, gpio.HIGH)

        while True:
            key = matrix.maps[matrix.now_layer]
            btns = [gpio.input(btn_gpio[k]) for k in btn_gpio]
            print(btns)
            if not gpio.input(btn_gpio[key]):
                time.sleep(0.1)
                if [gpio.input(btn_gpio[k]) for k in btn_gpio] != btns:
                    break
                while not gpio.input(btn_gpio[key]):
                    time.sleep(0.3)
                print('press')
                matrix.now_layer += 1

            time.sleep(1)
    finally:
        gpio.cleanup()
