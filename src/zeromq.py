# This file is ran on the Pi to send button status updates
# It uses ZeroMQ to send messages to a receiver
# Note that PI should use a virtual environment with the required packages installed
# Required packages: zmq, RPi.GPIO
# Follow the instructions in DEVELOPERS.md to set up the virtual environment and install the packages

import RPi.GPIO as GPIO
import time
import zmq

# Define the GPIO pin for the button
USER_BUTTON_GPIO_PIN = 6
# Setup GPIO
GPIO.setmode(GPIO.BCM)
# Use GPIO USER_BUTTON_GPIO_PIN for the button input
GPIO.setup(USER_BUTTON_GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.PUSH)

# Connect to the ZeroMQ server
# Replace with the actual IP address and port of the ZeroMQ server
socket.connect("tcp://10.0.0.119:5555")  

try:
    while True:
        # Send the button status to the ZeroMQ server
        input_state = GPIO.input(USER_BUTTON_GPIO_PIN)
        socket.send_string(f"Button status {input_state}!")
        time.sleep(0.5)
finally:
    GPIO.cleanup()
