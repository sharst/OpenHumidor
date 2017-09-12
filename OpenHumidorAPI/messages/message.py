#!/usr/bin/python

class Message(object):
    """
    Base message object that defines the fields and functions used in 
    both messages sent to and received from sensors.
    """
    RECEIVED_NOTHING = 1
    WRONG_MESSAGE_ID = 2
    WRONG_HEADER = 3
    SENSOR_NOT_FOUND = 4

    def __init__(self):
        self.address = None
        self.errorflags = None
        self.temperature = None
        self.humidity = None
        self.supply_v = None
        self.link_quality = None
        self.fan = None
        self.humidifier = None
        self.fire_again = None
        self.message_id = None

    def to_bytes(self):
        return None

    def from_bytes(self, bytearr):
        pass

    def calc_checksum(self, msg):
        return int(np.sum([ord(x) for x in msg])) & 0xFF
