import spidev


if __name__ == '__main__':
    register = spidev.SpiDev(clk=22, cs=27, mosi=17, miso=None, verbose=True)

    register.put(int("001000100111",2),12)
