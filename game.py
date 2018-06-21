import RPi.GPIO as gpio
import time
from threading import Thread

from matrix import LEDMatrix


def compare_layer(layer, btn_inputs):
    pass

def get_layer(name):
    name = [not int(n) for n in name]
    return name

if __name__ == '__main__':
    try:
        matrix = LEDMatrix(100)

        matrix.startPrint()

        gpio.setmode(gpio.BCM)
        btns = [
            {'name': '0001', 'gpio':21},
            {'name': '0010', 'gpio':20},
            {'name': '0100', 'gpio':16},
            {'name': '1000', 'gpio':12}
        ]
        for i in range(len(btns)):
            gpio.setup(btns[i]['gpio'], gpio.IN, pull_up_down=gpio.PUD_UP)

        layer = get_layer(matrix.maps[matrix.now_layer])
        print(layer)

        while True:
            btn_inputs = [gpio.input(b['gpio']) for b in btns]
            print("btns", btn_inputs)

            if layer == btn_inputs:
                time.sleep(0.1)

                while layer == btn_inputs:
                    time.sleep(0.1)

                print('press')
                matrix.now_layer += 1

                layer = get_layer(matrix.maps[matrix.now_layer])

            time.sleep(0.1)
    finally:
        gpio.cleanup()
