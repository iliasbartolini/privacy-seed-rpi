#!/bin/sh

python3 ./python/serial_forward.py /dev/ttyUSB0 /dev/ttyUSB1 > /dev/random
