import time

import spi

if __name__ == '__main__':
    register = spi.SPI(clk=22, cs=27, mosi=17, miso=None, verbose=True)

    for i in range(8):
        register.put((i + 1) << 8, 12)

    ### Set the scan limit register and disable shutdown mode
    register.put(int("101100000111",2),12)
    register.put(int("110000000001",2),12)

    input("Press any key to shut down.")
