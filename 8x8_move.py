import RPi.GPIO as gpio
import json, time, random

from register import Register

class LEDMatrix:
    def __init__(self, num_layer=20):
        self.DS =    [17, 13]
        self.SHCP =  [22, 26]
        self.STCP =  [27, 19]
        self.register = Register(DS, SHCP, STCP)

        # gpio setup
        gpio.setmode(gpio.BCM)
        for g in DS + SHCP + STCP:
            gpio.setup(g, gpio.OUT)

        self.now_layer = 0

        self.graph = self.makeGraph(num_layer)

    def show8x8(self, sec):
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
        for _ in range(int(100 * sec)):
            for i in range(8):
                register.shift(0, graph[i])

                register.shift(1, temp[i])
                time.sleep(0.001)
                register.shift(1, '11111111')

    def printOut(self, step=1, width=8, delay=1):
        for i in range(0, len(self.graph) - width + 1, step):
            graph_slice = self.graph[i:i + width]
            print("\n".join(graph_slice))
            print()

            # print to 8x8
            show8x8(graph_slice, sec=delay)

    def makeGraph(self, num_layer):
        with open('data/layer.json') as json_f:
            data = json.loads(json_f.read())
        keys = list(data.keys())

        graph = []
        for i in range(num_layer):
            r_int = random.randint(0, len(keys) - 1)
            graph += data[keys[r_int]]

        return graph

def makeWords(words):
    with open('data/hello.json') as json_f:
        data = json.loads(json_f.read())

    graph = []
    for w in words:
        graph += data[w]

    return graph

if __name__ == '__main__':
    try:
        matrix = LEDMatrix()

        matrix.printOut(delay=0.5)
    finally:
        gpio.cleanup()
