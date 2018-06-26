import RPi.GPIO as gpio
import time
from threading import Thread


def compare_layer(layer, btn_inputs):
    pass

def get_layer(name):
    name = [abs(int(n) - 1) for n in name]
    return name

if __name__ == '__main__':
    try:
        player = input('Please choose player1 or player2')
        
        if player == '1':
            from matrix import LEDMatrix
        else:
            from matrix_2p import LEDMatrix


        matrix = LEDMatrix(20)

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

        layer = get_layer(matrix.maps[matrix.now_layer])
        print(layer)

        while True:
            btn_inputs = [gpio.input(b['gpio']) for b in btns]
            print("btns", btn_inputs)

            # btn map == now_layer map
            if layer == btn_inputs:
                while layer == btn_inputs:
                    time.sleep(0.1)
                    btn_inputs = [gpio.input(b['gpio']) for b in btns]

                print('press')
                matrix.now_layer += 1

                layer = get_layer(matrix.maps[matrix.now_layer])
                print('layer', layer)

            time.sleep(0.1)
    finally:
        gpio.cleanup()
