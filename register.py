import RPi.GPIO as gpio
import time

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

def shift(i, shift_data):
    gpio.output(STCP, gpio.LOW)
    for d in shift_data:
        gpio.output(SHCP[i], gpio.LOW)
        gpio.output(DS[i], int(d))
        gpio.output(SHCP[i], gpio.HIGH)
    gpio.output(STCP, gpio.HIGH)

def hc_out(data):
    for each in data:
        gpio.output(STCP, gpio.LOW)
        shift(each)
        gpio.output(STCP, gpio.HIGH)

if __name__ =="__main__":
    try:
        setup()

        data = ['00001111', '11000000', '11111111', '00000000']
        data *= 3

        hc_out(data)
    finally:
        gpio.cleanup()
