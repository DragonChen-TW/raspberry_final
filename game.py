import RPi.GPIO as gpio
import time
from threading import Thread

from matrix import LEDMatrix


def comparelayer(btn_map):
    #print(matrix.maps[matrix.now_layer])
    if btn_map == matrix.maps[matrix.now_layer]:
        matrix.now_layer += 1

def find_key(name):
    for i in range(len(btns)):
        if btns[i]['name'] == name:
            return i
    return -1

if __name__ == '__main__':
    try:
        matrix = LEDMatrix(100)

        matrix.startPrint()

        gpio.setmode(gpio.BCM)
        btns = [
            {'name': '0001', 'gpio':12},
            {'name': '0010', 'gpio':16},
            {'name': '0100', 'gpio':20},
            {'name': '1000', 'gpio':21}
        ]
        for i in range(len(btns)):
            gpio.setup(btns[i]['gpio'], gpio.IN, pull_up_down=gpio.PUD_UP)

        now = find_key(matrix.maps[matrix.now_layer])

        while True:
            # btn_inputs = [gpio.input(b['gpio']) for b in btn_gpio]
            # print("btns", btn_inputs)

            if not gpio.input(btns[now]['gpio']):
                time.sleep(0.1)

                while not gpio.input(btns[now]['gpio']):
                    time.sleep(0.1)

                print('press')
                matrix.now_layer += 1

            time.sleep(0.1)
    finally:
        gpio.cleanup()
