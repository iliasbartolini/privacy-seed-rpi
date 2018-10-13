#!/usr/bin/env python3

import serial
import sys
from pprint import pprint

if (len(sys.argv) != 3):
    print( "command line: serial_forward.py device_port_1 device_port_2" )
    sys.exit()

device_port_1 = sys.argv[1]
device_port_2 = sys.argv[2]

serial_1 = serial.Serial(device_port_1, 115200, timeout = 5)
serial_1.setDTR()

serial_2 = serial.Serial(device_port_2, 115200, timeout = 5)
serial_2.setDTR()

device_name_1 = serial_1.readline().decode().rstrip()
device_name_2 = serial_2.readline().decode().rstrip()

if "HRT" in device_name_1:
    serial_input = serial_1
elif "DotStar" in device_name_1:
    serial_output = serial_1
else:
    raise Exception("I/O device {} on {} not recognized".format(device_name_1, device_port_1))

if "HRT" in device_name_2:
    serial_input = serial_2
elif "DotStar" in device_name_2:
    serial_output = serial_2
else:
    raise Exception("I/O device {} on {} not recognized".format(device_name_2, device_port_2))

while 1:
    input_byte = serial_input.read()
    serial_output.write(input_byte)
    sys.stdout.buffer.write(input_byte)
    sys.stdout.flush()
