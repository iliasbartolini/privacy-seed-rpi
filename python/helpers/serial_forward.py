import serial
import sys

if (len(sys.argv) != 3):
    print( "command line: serial_forward.py input_port output_port" )
    sys.exit()

serial_input_port = sys.argv[1]
serial_output_port = sys.argv[2]

serial_input = serial.Serial(serial_input_port, 115200)
serial_input.setDTR()
serial_input.flush()

serial_output = serial.Serial(serial_output_port, 115200)
serial_output.setDTR()

while 1:
    input_byte = serial_input.read()
    serial_output.write(input_byte)
    sys.stdout.write(input_byte)
    sys.stdout.flush()
