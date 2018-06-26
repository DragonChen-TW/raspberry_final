import RPi.GPIO as gpio
import json, time, random
from threading import Thread

class Register:
    def __init__(self, DS, SHCP, STCP):
        self.DS = DS
        self.SHCP = SHCP
        self.STCP = STCP

        gpio.setmode(gpio.BCM)
        for g in self.DS + self.SHCP + self.STCP:
            gpio.setup(g, gpio.OUT)

    def makeTick(self, gpio_num):
        gpio.output(gpio_num, gpio.HIGH)
        gpio.output(gpio_num, gpio.LOW)

    def shift(self, i, shift_data):
        for d in shift_data:
            gpio.output(self.DS[i], int(d))
            self.makeTick(self.SHCP[i])
        self.makeTick(self.STCP[i])

class LEDMatrix:
    def __init__(self, num_layer=20):
        # DS, SHCP, STCP
        # CLK, CS, DIN
        self.DS =    [22]
        self.SHCP =  [27]
        self.STCP =  [17]

        self.now_layer = 0
        self.max_layer = num_layer

        self.maps, self.graph = self.makeGraph(num_layer)

    def show8x8(self, graph_s, sec):
        address = ['0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000']
        for i in range(8):
            self.register.shift(0, address[i] + graph_s[i])
            time.sleep(1)

    def startPrint(self, step=2, width=8, delay=1):
        self.th = Thread(target=self._startPrint, args=(step, width, delay,))
        self.th.start()
        # th.join()

    def _startPrint(self, step, width, delay):
        self.register = Register(self.DS, self.SHCP, self.STCP)
        # setting disable shutdown and sacan limit
        self.register.shift(0, '101100000111')
        self.register.shift(0, '110000000001')
        while self.now_layer < self.max_layer:
            print(self.now_layer)
            i = self.now_layer * 2
            graph_slice = self.graph[i : i + width]

            # print to 8x8
            self.show8x8(graph_slice, sec=delay)

    def makeGraph(self, num_layer):
        with open('data/layer.json') as json_f:
            data = json.loads(json_f.read())
        # keys = list(data['one_layer'].keys()) + list(data['two_layer'].keys())
        # print(keys)

        maps = []
        graph = []
        for i in range(num_layer):
            r_int = random.randint(1, 10)
            if r_int <= 7:
                keys = list(data['one_layer'].keys())
                r_int = random.randint(0, len(keys) - 1)

                maps.append(keys[r_int])
                graph += data['one_layer'][keys[r_int]]
            else:
                keys = list(data['two_layer'].keys())
                r_int = random.randint(0, len(keys) - 1)

                maps.append(keys[r_int])
                graph += data['two_layer'][keys[r_int]]


        # to think
        graph += ["00000000"] * 8

        return maps, graph

def makeWords(words):
    with open('data/hello.json') as json_f:
        data = json.loads(json_f.read())

    graph = []
    for w in words:
        graph += data[w]

    return graph

if __name__ == '__main__':
    try:
        matrix = LEDMatrix(10)

        matrix.startPrint()

        while True:
            time.sleep(1)
    finally:
        gpio.cleanup()
