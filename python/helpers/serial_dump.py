import serial
import sys

def get_port_from_command_line_arguments():
    if (len(sys.argv) != 2):
       print( "command line: serial_dump.py serial_port" )
       sys.exit()
    return sys.argv[1]

serial_port = get_port_from_command_line_arguments()

ser = serial.Serial(serial_port, 115200)
ser.setDTR()

ser.flush()

while 1:
   sys.stdout.buffer.write(ser.read()) #RAW data
   # sys.stdout.write(ser.readline().decode())
   sys.stdout.flush()
