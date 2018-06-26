import RPi.GPIO as gpio
import time, LED

if __name__ == '__main__':
    try:
        gpio.setmode(gpio.BCM)
        gpio.setmode(20,gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setmode(21,gpio.IN, pull_up_down=gpio.PUD_UP)

        while True:
            if not gpio.input(20):
                print('press 20 ')
            elif not gpio.input(21):
                print('press 21 ')
            else:
                print("no press")
                

            time.sleep(0.5)
    finally:
        gpio.clenaup()
