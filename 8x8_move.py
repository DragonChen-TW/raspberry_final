import RPi.GPIO as gpio
import json, time, random

from register import Register

def setup():
    # global variables
    global DS, SHCP, STCP
    global register
    # global CLK, MOSI, CE
    # gpio left -----OOO--------000-
    DS =    [17, 13]
    SHCP =  [22, 26]
    STCP =  [27, 19]

    # gpio setup
    gpio.setmode(gpio.BCM)
    for g in DS + SHCP + STCP:
        gpio.setup(g, gpio.OUT)

    # register and init LED
    register = Register(DS, SHCP, STCP)
    register.shift(1, '11111111')

def show8x8(graph, sec):
    global register
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

def print8x8(graph, step=1, width=8, delay=1):
    for i in range(0, len(graph) - width + 1, step):
        graph_slice = graph[i:i + width]
        print("\n".join(graph_slice))
        print()

        # print to 8x8
        show8x8(graph_slice, sec=delay)

        # time.sleep(delay)

def makeGraph(num_layer):
    with open('data/layer.json') as json_f:
        data = json.loads(json_f.read())
    keys = data.keys()

    graph = []
    for i in range(num_layer):
        r_int = random.randint(0, len(keys))
        graph.append(data[keys[r_int]])

def makeWords(words):
    with open('data/hello.json') as json_f:
        data = json.loads(json_f.read())

    graph = []
    for w in words:
        graph += data[w]

    return graph

if __name__ == '__main__':
    try:
        setup()

        gpio.input(12)

        # words = "hello"
        # graph = makeWords(words)
        graph(20)
        print(graph)
        # print8x8(graph, delay=0.5)
    finally:
        gpio.cleanup()
