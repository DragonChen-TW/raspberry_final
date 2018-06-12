import RPi.GPIO as gpio
import time, LED

if __name__ == '__main__':
    try:
        gpio.setmode(gpio.BCM)
        LED.setup(12, 'in')
        LED.setup(21, 'out')

        while True:
            if not gpio.input(12):
                print('press')
                LED.turnON(21)
            else:
                LED.turnOFF(21)

            time.sleep(0.5)
    finally:
        gpio.clenaup()
