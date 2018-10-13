#!/bin/sh

python3 ./python/helpers/serial_forward.py /dev/ttyUSB0 /dev/ttyUSB1 > /dev/random
