import time

import spi

if __name__ == '__main__':
    register = spi.SPI(clk=22, cs=27, mosi=17, miso=None, verbose=True)

    for i in range(16):
        register.put((i + 1) << 8, 12)

    ### Set the scan limit register and disable shutdown mode
    register.put(int("101100000111",2),12)
    register.put(int("110000000001",2),12)

    # register.put(int('010011100111', 2), 12)

    heart = [
        '00000000',
        '01100110',
        '11111111',
        '11111111',
        '01111110',
        '00111100',
        '00011000',
        '00000000',
    ]

    for i in range(8):
        loc = (i + 1) << 8
        register.put(loc + int(heart[i], 2), 12)


    input("Press any key to shut down.")
