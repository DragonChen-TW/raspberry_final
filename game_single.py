import RPi.GPIO as gpio
import time
from threading import Thread

from register import Register
from matrix_p2 import Matrix

class LEDMatrix_p1(Matrix):
    def __init__(self, *args, **kwargs):
        self.DS =    [17, 13]
        self.SHCP =  [22, 26]
        self.STCP =  [27, 19]

        super().__init__(*args, **kwargs)

    def show8x8(self, graph_s):
        temp = [
            '11111110',
            '11111101',
            '11111011',
            '11110111',
            '11101111',
            '11011111',
            '10111111',
            '01111111',
        ]
        for i in range(8):
            self.register.shift(0, graph_s[i][::-1])

            self.register.shift(1, temp[i])
            time.sleep(0.001)
            self.register.shift(1, '11111111')

    def startPrint(self):
        self.register = Register(self.DS, self.SHCP, self.STCP)

        self.printLoop()

class LEDMatrix_p2(Matrix):
    def __init__(self, *args, **kwargs):
        self.DS =    [17]
        self.SHCP =  [22]
        self.STCP =  [27]

        super().__init__(*args, **kwargs)

    def show8x8(self, graph_s):
        # address = ['0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000']
        address = ['1000','0111','0110','0101','0100','0011','0010','0001']
        for i in range(8):
            self.register.shift(0, address[i] + graph_s[i])

    def startPrint(self):
        self.register = Register(self.DS, self.SHCP, self.STCP)
        # setting disable shutdown and sacan limit
        self.register.shift(0, '101100000111')
        self.register.shift(0, '110000000001')

        self.printLoop()

def get_layer(name):
    name = [abs(int(n) - 1) for n in name]
    return name

if __name__ == '__main__':
    try:
        player = input('Please choose player1 or player2: ')

        if player == '1':
            matrix = LEDMatrix_p1(50)
        else:
            matrix = LEDMatrix_p2(50)

        th = Thread(target=matrix.startPrint)
        th.start()

        gpio.setmode(gpio.BCM)
        btns = [
            {'name': '1000', 'gpio':21},
            {'name': '0100', 'gpio':20},
            {'name': '0010', 'gpio':16},
            {'name': '0001', 'gpio':12}
        ]
        for i in range(len(btns)):
            gpio.setup(btns[i]['gpio'], gpio.IN, pull_up_down=gpio.PUD_UP)

        layer = get_layer(matrix.maps[matrix.now_layer])
        print(layer)

        while True:
            btn_inputs = [gpio.input(b['gpio']) for b in btns]
            # print("btns", btn_inputs)

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
