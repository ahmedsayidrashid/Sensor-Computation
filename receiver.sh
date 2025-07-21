#!/bin/bash 

# Compile the receiver code
g++ src/receiver.cpp -o output/receiver -lzmq

# Add a little delay (to make it look cool :))
sleep 1

# Run the receiver code
./output/receiver
