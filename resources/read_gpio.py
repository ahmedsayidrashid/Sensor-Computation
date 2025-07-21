# This file is ran on the Raspberry Pi to read GPIO pin states
# It was mainly used for testing purposes
# Note that this file is NOT a requirement for the main functionality

import RPi.GPIO as GPIO
import time

READ_GPIO = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(READ_GPIO, GPIO.IN) 

try:
    while True:
        state = GPIO.input(READ_GPIO)
        print("Pin state:", state)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

