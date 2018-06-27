import RPi.GPIO as gpio
import json, time, random, requests
from threading import Thread

from register import Register

class Matrix:
    def __init__(self, num_layer=20, online=False, game_id=None, p_name=None):
        self.now_layer = 0
        self.max_layer = num_layer
        self.player = ""

        if online:
            self.game_id = game_id
            self.maps, self.graph = self.getGraph(game_id, p_name)
        else:
            self.maps, self.graph = self.makeGraph(num_layer)

    def printLoop(self):
        while self.now_layer < self.max_layer:
            # print(self.now_layer, end='')
            i = self.now_layer * 2
            graph_slice = self.graph[i : i + 8]

            # print to 8x8
            self.show8x8(graph_slice)

    def getGraph(self, game_id, p_name):
        url = 'http://140.117.71.66:8000/game/update/?game_id={}&player=reset'.format(game_id)
        requests.get(url)

        url = 'http://140.117.71.66:8000/game/graph/?id={}'.format(self.game_id)

        res = requests.get(url)
        res = json.loads(res.text)

        return res['maps'], res['graph']

    def makeGraph(self, num_layer):
        with open('data/layer.json') as json_f:
            data = json.loads(json_f.read())

        maps = []
        graph = []
        for i in range(num_layer):
            r_int = random.randint(1, 10)
            if r_int <= 7:
                sub_data = data['one_layer']
            else:
                sub_data = data['two_layer']

            keys = list(sub_data.keys())
            r_int = random.randint(0, len(keys) - 1)

            maps.append(keys[r_int])
            graph += sub_data[keys[r_int]]


        # to think
        graph += ["00000000"] * 8

        return maps, graph

    def reqNext(self):
        url = 'http://140.117.71.66:8000/game/update/?game_id={}&player={}'.format(self.game_id, self.player)
        res = requests.get(url)

    def makeWords(words):
        with open('data/hello.json') as json_f:
            data = json.loads(json_f.read())

        graph = []
        for w in words:
            graph += data[w]

        return graph

class LEDMatrix_p1(Matrix):
    def __init__(self, *args, **kwargs):
        self.DS =    [17, 13]
        self.SHCP =  [22, 26]
        self.STCP =  [27, 19]

        self.player = 'p1'

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

        self.player = 'p2'

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
