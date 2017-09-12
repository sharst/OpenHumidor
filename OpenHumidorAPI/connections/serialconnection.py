from messages.sensormessage import SensorMessage
from messages.basemessage import BaseMessage
from connections.connection import Connection
import serial
from sensortools.tools import log_info

class SerialConnection(Connection):
    def __init__(self, device):
        super(SerialConnection, self).__init__()
        self.name = "SerialConnection"
        self.device = device
        self.init_adapter()
        log_info("SerialConnection initialized.")

    def init_adapter(self):
        self.ser = serial.Serial(self.device, 9600, timeout=.2)
        self.ser.read(self.ser.inWaiting())

    def receive_bytes(self):
        try:
            if self.ser.inWaiting() >= SensorMessage.BYTE_LENGTH:
                self.rx_byte_buf += self.ser.read(self.ser.inWaiting())
        except serial.SerialException:
            log_info("Catched some error, reinit adapter")
            self.init_adapter()
        except AttributeError:
            log_info("Catched some error, reinit adapter")
            self.init_adapter()

    def send_bytes(self):
        try:
            self.ser.write(self.tx_byte_buf)
            self.tx_byte_buf = ""
        except serial.SerialException:
            log_info("Catched some error, reinit adapter")
            self.init_adapter()
        except AttributeError:
            log_info("Catched some error, reinit adapter")
            self.init_adapter()

