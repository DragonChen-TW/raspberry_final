import RPi.GPIO as gpio
import time

def setupAll():
    gpio.setmode(gpio.BCM)
    global col_led, row_led
    for i in col_led + row_led:
        try:
            gpio.setup(i, gpio.OUT)
        except:
            print(str(i) + "wasn't be setuped.")
def cleanAll():
    global col_led, row_led
    for i in row_led:
        gpio.output(i, gpio.LOW)
    for i in col_led:
        gpio.output(i, gpio.HIGH)
    gpio.cleanup()

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


col_led = [17, 27, 22, 5, 6, 13, 19, 26]
row_led = [15, 18, 23, 24, 12, 16, 20, 21]

if __name__ == '__main__':
    try:
        setupAll()

        temp1 = [0, 1]
        temp2 = [1, 0]
        icon = [temp1 * 4, temp2 * 4] * 4

        print(icon)

        show8x8(icon, 5)

        time.sleep(10)
    finally:
        cleanAll()
