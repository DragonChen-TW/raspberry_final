#!/usr/bin/env python
# File rpi_7219a.py
# http://www.bristolwatch.com/index.htm
# By Lewis Loflin - lewis@bvu.net

# Here we connect a MAX7219 8-digit module to display a
# count from 0-9999 after each digit converted to BCD format.
# The loop can be ended before count is finished by pressing Sw1.

# Two bytes are shifted in first being address, second being data.
# Works the same as two 74165 SSRs in series or 16-bits.
# LD "pulseCS()" clocks 16-bit address/data into working registers.



# access to GPIO must be through root
import RPi.GPIO as GPIO
import time

GPIO.setup(GPIO.BCM)

LATCH = 27 # CS
CLK = 22
dataBit = 17 # DIN


GPIO.setup(LATCH, GPIO.OUT) # P0
GPIO.setup(CLK, GPIO.OUT) # P1
GPIO.setup(dataBit, GPIO.OUT) # P7


# Setup IO
GPIO.output(11, 0)
GPIO.output(CLK, 0)


def pulseCLK():
    GPIO.output(CLK, 1)
    # time.sleep(.001)
    GPIO.output(CLK, 0)
    return

def pulseCS():
    GPIO.output(LATCH, 1)
    # time.sleep(.001)
    GPIO.output(LATCH, 0)
    return



# shift byte into MAX7219
# MSB out first!
def ssrOut(value):
    for  x in range(0,8):
        temp = value & 0x80
        if temp == 0x80:
           GPIO.output(dataBit, 1) # data bit HIGH
        else:
           GPIO.output(dataBit, 0) # data bit LOW
        pulseCLK()
        value = value << 0x01 # shift left
    return



# initialize MAX7219 4 digits BCD
def initMAX7219():

    # set decode mode
    ssrOut(0x09) # address
    #	ssrOut(0x00); // no decode
    ssrOut(0xFF) # 4-bit BCD decode eight digits
    pulseCS();

    # set intensity
    ssrOut(0x0A) # address
    ssrOut(0x04) # 9/32s
    pulseCS()

    # set scan limit 0-7
    ssrOut(0x0B); # address
    ssrOut(0x07) # 8 digits
    # ssrOut(0x03) # 4 digits
    pulseCS()


    # set for normal operation
    ssrOut(0x0C) # address
    # ssrOut(0x00); // Off
    ssrOut(0x01)  # On
    pulseCS()
	# clear to all 0s.
    for x in range(0,9):
        ssrOut(x)
        ssrOut(0x0f)
        pulseCS()
    return


def writeMAX7219(data, location):
    ssrOut(location)
    ssrOut(data)
    pulseCS()
    return


def displayOff():
   # set for normal operation
    ssrOut(0x0C) # address
    ssrOut(0x00); # Off
    # ssrOut(0x01)  # On
    pulseCS()


def displayOn():
   # set for normal operation
    ssrOut(0x0C) # address
    # ssrOut(0x00); # Off
    ssrOut(0x01)  # On
    pulseCS()



initMAX7219()

# Converts four digits in i into 4 BDC bytes.
# The writes digits to MAX7219.

for i in range(0, 9999):
    j = i
    # get 1st digit j
    for k in range(1, 4):
        digit = j % 10
        writeMAX7219(digit, k)
        j = j / 10


displayOff()

# print "Good by!"
