from messages.message import Message
import struct
from sensortools.tools import format_hex

class SensorMessage(Message):
    """
    Message object for messages received from a sensor
    """
    BYTE_LENGTH = 18

    def __init__(self, bytearr=None):
        super(SensorMessage, self).__init__()
        if bytearr is not None:
            self.from_byte_string(bytearr)

    def __repr__(self):
        out = "SensorMessage #{}\n".format(self.message_id)
        if self.temperature is not None:
            out += "Received from: \t\t\t{}\n".format(format_hex(self.address))
            out += "Error Flags: \t\t\t{}\n".format(bin(self.errorflags))
            out += "Temperature: \t\t\t{} C\n".format(self.temperature / 100.)
            out += "Humidity: \t\t\t{}%\n".format(self.humidity / 100.)
            out += "Supply Voltage: \t\t{}V\n".format(self.supply_v / 1000.)
            out += "Link quality: \t\t\t{}\n".format(self.link_quality)
            out += ""
        else:
            out += "Message fields not set yet.\n"
            out += "\n"
        return out

    def from_byte_string(self, bytestr):
        """
        Create a sensormessage-object from a formatted hex string, i.e.
        CA5559A660A18A020ACE11940FB600005000
        """
        bytearr = bytearray.fromhex(bytestr)
        self.from_bytes(bytes(bytearr))

    def from_bytes(self, bytearr):
        """
        Create a sensormessage-object from a bytestring, i.e.
        '\xcaUY\xa6`\xa1\x8a\x00\t2\x1b\xe1\x0f\x9a\x00\x00\x00\x00'
        """
        if len(bytearr) >= SensorMessage.BYTE_LENGTH:
            if len(bytearr) > SensorMessage.BYTE_LENGTH:
                bytearr = bytearr[:SensorMessage.BYTE_LENGTH+1]
            if bytearr[0] == "\xca" and bytearr[1] == "\x55":
                # Checksum checking is taken care of at RF module.
                #if self.calc_checksum(bytearr[:-1]) == ord(bytearr[-1]):
                self.address = bytearr[2:7]
                try:
                     (self.errorflags,
                     self.temperature,
                     self.humidity,
                     self.supply_v,
                     self.link_quality,
                     self.message_id) = struct.unpack(">BHHHBH", bytearr[7:17])
                except:
                    print "Failed to unpack message: " + format_hex(bytearr[7:])
                #else:
                #    raise ValueError("Incorrect checksum: Given: " + repr(ord(bytearr[-1])) + ", calc.: " + repr(self.calc_checksum(bytearr[:-1])))
            else:
                raise ValueError("Incorrect message header!")


    def to_bytes(self):
        bytearr = "\xca\x55" + self.address + struct.pack(">BHHHBHB", self.errorflags, self.temperature, self.humidity, self.supply_v, self.link_quality, self.message_id, 255)
        #bytearr += struct.pack(">B", self.calc_checksum(bytearr))
        return bytearr
