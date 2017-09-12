#!/usr/bin/python
import struct
from messages.message import Message
from sensortools.tools import log_info

class BaseMessage(Message):
    """
    Message object for messages sent from base to sensor
    """
    def __init__(self, address, devices, humidifier, fan, fire_again, message_id):
        super(BaseMessage, self).__init__()
        self.address = address
        self.humidifier = humidifier
        self.fan = fan
        self.fire_again = fire_again
        self.message_id = message_id;

    def __repr__(self):
        out = "BaseMessage #{}".format(self.message_id)
        if self.humidifier is not None:
            out += "Switch Humidifier: \t\t\t{}\n".format("ON" if self.humidifier else "OFF")
            out += "Switch Fan: \t\t\t{}%\n".format("ON" if self.fan else "OFF")
            out += "Fire again in: \t\t{}s \n".format(self.fire_again / 10.)
            out += "\n"
        else:
            out += "Message fields not set yet.\n"
            out += "\n"

    def to_bytes(self):
        """
        Create a series of bytes from this basemessage object, to send to one of the sensors
        """
        try:
            msg = self.address
            msg += "\xca\x55"
            msg += struct.pack(">BBHHBBBBBBBBBB", self.humidifier, self.fan, self.fire_again, self.message_id, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255)
            #msg += struct.pack(">B", self.calc_checksum(msg[5:]))
            return msg
        except struct.error:
            log_info("Couldn't parse message into bytes!")
