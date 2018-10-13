import serial
import sys
import io

if (len(sys.argv) != 2):
    print( "command line: serial_device_discovery.py input_port" )
    sys.exit()

serial_input_port = sys.argv[1]

serial_input = serial.Serial(serial_input_port, 115200, timeout = 5)
serial_input.setDTR()

device_name = serial_input.readline()
print("Device name:")
print(device_name)

print("Data forward:")
while 1:
    input_byte = serial_input.read()
    # serial_output.write(input_byte)
    sys.stdout.write(input_byte)
    sys.stdout.flush()
