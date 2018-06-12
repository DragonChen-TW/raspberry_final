import json, time
from pprint import pprint

def setup():
    # global variables
    global DS, SHCP, STCP
    # global CLK, MOSI, CE
    # gpio left -----OOO--------000-
    DS =    [17, 13]
    SHCP =  [27, 29]
    STCP =  [22, 26]

    gpio.setmode(gpio.BCM)
    for g in DS + SHCP + STCP:
        gpio.setup(g, gpio.OUT)

def show8x8(image, sec):
    for _ in range(int(100 * sec)):
        for i in range(1):
            for j in range(8):
                if image[i][j]:
                    # gpio.output(row_led[j], gpio.HIGH)
                    print('1')
                else:
                    # gpio.output(row_led[j], gpio.LOW)
                    print('0')
            # gpio.output(col_led[i], gpio.LOW)
            # time.sleep(0.01)
            # gpio.output(col_led[i], gpio.HIGH)

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
    words = "hello"

    print8x8(words, delay=0.5)
