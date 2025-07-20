import zmq
import RPi.GPIO as GPIO
import time

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://10.0.0.119:5555")  # change to your PC's IP and port

try:
    while True:
        input_state = GPIO.input(6)
        if 1: # always print the buttons status
            socket.send_string(f"Button status {input_state}!")
            time.sleep(0.5)
finally:
    GPIO.cleanup()
