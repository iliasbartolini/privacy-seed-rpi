#!/usr/bin/env python3

import sys
from serial_device_discovery import SerialDeviceDiscovery
from random_entropy_adder import RandomEntropyAdder
from sound_mixer import SoundMixer
from pprint import pprint

HRT_SENSOR_UNCOVERED = b'\x00'
HRT_SENSOR_COVERED   = b'\x01'
HRT_SENSOR_BEAT_RATE = b'\x02'
HRT_SENSOR_MAGIC     = b'\x03' # don't try me... seriously! :)

if (len(sys.argv) != 3):
    print( "command line: privacy_seed.py device_port_1 device_port_2" )
    sys.exit()


sound_mixer = SoundMixer()
sound_mixer.play_base()

io_devices = SerialDeviceDiscovery(sys.argv[1], sys.argv[2])

with RandomEntropyAdder() as random_entropy_adder:
    while 1:
        input_byte = io_devices.serial_input.read()
        io_devices.serial_output.write(input_byte)
        io_devices.serial_output.flush()

        if input_byte == HRT_SENSOR_UNCOVERED:
            sys.stdout.write('.')
        elif input_byte == HRT_SENSOR_COVERED:
            data_byte = io_devices.serial_input.read()
            io_devices.serial_output.write(data_byte)
            io_devices.serial_output.flush()
            random_entropy_adder.add_entropy(data_byte)
            sys.stdout.write('*')
        elif input_byte == HRT_SENSOR_BEAT_RATE:
            data_byte = io_devices.serial_input.read()
            sound_mixer.play_heartbeat()
            io_devices.serial_output.write(data_byte)
            io_devices.serial_output.flush()
            hrt_rate = int.from_bytes(data_byte, byteorder='big', signed=False)
            sys.stdout.write('\nheart rate: {}\n'.format(hrt_rate))
        elif input_byte == HRT_SENSOR_MAGIC:
            sys.stdout.write('\nMAGIC!\n')
        else:
            unknown_command = int.from_bytes(input_byte, byteorder='big', signed=False)
            sys.stdout.write('\nUnknown HRT command: {}\n'.format(int.from_bytes(unknown_command)))

        sys.stdout.flush()
