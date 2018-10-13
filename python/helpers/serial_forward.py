#!/usr/bin/env python3

import sys
from serial_device_discovery import SerialDeviceDiscovery

if (len(sys.argv) != 3):
    print( "command line: serial_forward.py device_port_1 device_port_2" )
    sys.exit()

io_devices = SerialDeviceDiscovery(sys.argv[1], sys.argv[2])

while 1:
    input_byte = io_devices.serial_input.read()
    io_devices.serial_output.write(input_byte)
    sys.stdout.buffer.write(input_byte)
    sys.stdout.flush()
