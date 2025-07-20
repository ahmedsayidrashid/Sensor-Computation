import RPi.GPIO as GPIO
import time

READ_GPIO = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(READ_GPIO, GPIO.IN)  # use GPIO "READ_GPIO"

try:
    while True:
        state = GPIO.input(READ_GPIO)
        print("Pin state:", state)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

