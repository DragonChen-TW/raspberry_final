import RPi.GPIO as gpio
import time

def setup():
    global gpio_tri, gpio_echo
    gpio.setmode(gpio.BCM)
    gpio_tri = 7
    gpio_echo = 12

    gpio.setup(gpio_tri, gpio.OUT)
    gpio.setup(gpio_echo, gpio.IN)

def send_trigger():
    global gpio_tri
    gpio.output(gpio_tri, gpio.HIGH)
    time.sleep(0.00001)
    gpio.output(gpio_tri, gpio.LOW)

def get_speed():
    speed = 33100 + 26 * 60
    return speed

def get_distance():
    global gpio_echo
    send_trigger()

    start_t = 0
    stop_t = 0
    while gpio.input(gpio_echo) == 0:
        start_t = time.time()
    while gpio.input(gpio_echo) == 1:
        stop_t = time.time()

    time_elapsed = stop_t - start_t
    speed = get_speed()
    distance = (time_elapsed * speed) / 2

    return distance

if __name__ == '__main__':
    try:
        setup()

        while True:
            dist = get_distance()
            print('Measured Distance = {}'.format(dist))

            time.sleep(1)
    finally:
        gpio.cleanup()
