import json, time

from register import Register

def setup():
    # global variables
    global DS, SHCP, STCP
    # global CLK, MOSI, CE
    # gpio left -----OOO--------000-
    DS =    [17, 13]
    SHCP =  [22, 26]
    STCP =  [27, 29]

    gpio.setmode(gpio.BCM)
    for g in DS + SHCP + STCP:
        gpio.setup(g, gpio.OUT)

def show8x8(graph, sec=2):
    global register
    temp = [
        '10000000',
        '01000000',
        '00100000',
        '00010000',
        '00001000',
        '00000100',
        '00000010',
        '00000001',
    ]
    # for _ in range(int(100 * sec)):
    for i in range(8):
        register.shift(0, graph[i])

        register.shift(1, '00000000')
        time.sleep(0.01)
        register.shift(1, temp[i])
    time.sleep(10)


def print8x8(words, step=1, width=8, delay=1):
    graph = makeGraph(words)

    for i in range(0, len(graph) - width + 1, step):
        graph_slice = graph[i:i + width]
        print("\n".join(graph_slice))
        print()

        # print to 8x8
        show8x8(graph_slice, sec=delay)

        time.sleep(delay)

def makeGraph(words):
    with open('data/hello.json') as json_f:
        data = json.loads(json_f.read())

    graph = []
    for w in words:
        graph += data[w]

    return graph

if __name__ == '__main__':
    setup()
    register = Register(DS, SHCP, STCP)

    # words = "hello"
    # print8x8(words, delay=0.5)

    t = ['11110000'] * 4 + ['00001111'] * 4
    show8x8(t)
