#!/usr/bin/python
from messages.sensormessage import SensorMessage
import time

class DataLogger(object):
    """
    An object that is used to log data from OpenHumidor
    sensors into a csv-file
    """
    def __init__(self, fn):
        self.file = open(fn, "a")

    def log(self, msg):
        if type(msg) == SensorMessage:
            self.file.write("{:.2f},{},{},{},{},{},{}\n".format(time.time(),
                                                       msg.message_id,
                                                       bin(msg.errorflags),
                                                       msg.temperature / 100.,
                                                       msg.humidity / 100.,
                                                       msg.supply_v / 1000.,
                                                       msg.link_quality))
            self.file.flush()

    def shutdown(self):
        self.file.close()
