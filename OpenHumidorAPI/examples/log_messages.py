#!/usr/bin/python
import time
from sensor_interface import SensorInterface
from connections.serialconnection import SerialConnection
from sensortools.data_logger import DataLogger

fn = "sensor_readings_{:.0f}.csv".format(time.time() * 100)
dl = DataLogger(fn)

def callback(msg):
    print "New message recorded:"
    print msg
    print ""
    dl.log(msg)

if __name__ == "__main__":
    interf = SensorInterface()
    interf.register_callback(callback)
    interf.attach_connection(SerialConnection("/dev/openhumidor_debug"))
    interf.start()
    raw_input("Press enter to stop recording")
    print "Done. Saved recorded data to " + fn
    interf.shutdown()
    interf.join()
