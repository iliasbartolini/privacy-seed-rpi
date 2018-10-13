import serial

HEART_RATE_SENSOR_ID = "HRT"
DOTSTAR_LED_CONTROLLER_ID = "DotStar"

class SerialDeviceDiscovery:

    def __init__(self, device_port_1, device_port_2):
        self.port_discovery(device_port_1)
        self.port_discovery(device_port_2)

    def port_discovery(self, device_port):
        serial_port = serial.Serial(device_port, 115200, timeout = 5)
        serial_port.setDTR()
        device_name = serial_port.readline().decode().rstrip()

        if HEART_RATE_SENSOR_ID in device_name:
            self.serial_input = serial_port
        elif DOTSTAR_LED_CONTROLLER_ID in device_name:
            self.serial_output = serial_port
        else:
            raise Exception("I/O device {} on {} not recognized".format(device_name, device_port))
