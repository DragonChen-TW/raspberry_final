import json, time
from pprint import pprint

def show8x8(image, sec):
    for _ in range(int(1000 * sec)):
        for i in range(8):
            for j in range(8):
                if image[i][j]:
                    gpio.output(row_led[j], gpio.HIGH)
                else:
                    gpio.output(row_led[j], gpio.LOW)
            gpio.output(col_led[i], gpio.LOW)
            time.sleep(0.001)
            gpio.output(col_led[i], gpio.HIGH)

def print8x8(words, step=1, width=8, delay=1):
    graph = makeGraph(words)

    for i in range(0, len(graph) - width + 1, step):
        graph_slice = graph[i:i + width]

        print("\n".join(graph_slice))
        print()

        # print to 8x8

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
