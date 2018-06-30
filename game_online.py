import RPi.GPIO as gpio
import time
from threading import Thread
from pygame.mixer import init
from pygame.mixer import music

from matrix import LEDMatrix_p1, LEDMatrix_p2
from ultra import *

def get_layer(name):
    name = [abs(int(n) - 1) for n in name]
    return name

def playOffline(matrix):
    mp3 = ['small.mp3', 'hihat.mp3', 'down.mp3', 'snare.mp3']
    now = matrix.maps[matrix.now_layer]
    # print('=====', self.maps[self.now_layer], '=====')
    # print('-----', now.index('1'), '-----')
    init()
    music.load('music/' + mp3[now.index('1')])
    music.play()

if __name__ == '__main__':
    try:
        player = input('Please choose player1 or player2: ')
        online = input('If enter a online game room?(y/n): ')
        if online == 'y':
            game_id = int(input('Then, please input game room\'s id: '))
            p_name = input('Please input your NickName: ')
            online = True
        else:
            game_id = None
            p_name = ''
            online = False

        if player == '1':
            matrix = LEDMatrix_p1(50, online=online, game_id=game_id, p_name=p_name)
        else:
            matrix = LEDMatrix_p2(50, online=online, game_id=game_id, p_name=p_name)



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
                if online:
                    th2 = Thread(target=matrix.reqNext)
                    th2.start()
                else:
                    th2 = Thread(target=playOffline, args=(matrix,))
                    th2.start()

                layer = get_layer(matrix.maps[matrix.now_layer])
                print('layer', layer)

            time.sleep(0.1)
    finally:
        final_graph = [
            '10001000',
            '10101000',
            '01010000',
            '00111000',
            '00010000',
            '00111101',
            '00000111',
            '00000101'
        ]
        matrix.show8x8(final_graph[::-1])
        gpio.cleanup()
