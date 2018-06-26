import time

import spi

if __name__ == '__main__':
    register = spi.SPI(clk=22, cs=27, mosi=17, miso=None, verbose=True)

    for i in range(8):
        register.put((i + 1) << 8, 12)

    ### Set intensity low
    register.put(int("101000000000",2), 16)
    register.put(int("001000100111",2),12)
    time.sleep(1)

    ### Enable all digits in scan-limit register
    register.put(int("101100000111",2), 16)
    register.put(int("001000100111",2),12)
    time.sleep(1)

    input("Press any key to shut down.")
