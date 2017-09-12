#!/usr/bin/python
import threading
from messages.sensormessage import SensorMessage
import time
from sensortools.tools import log_info

class Connection(threading.Thread):
    def __init__(self):
        self.running = True
        self.rx_msg_buf = []
        self.tx_msg_buf = []
        self.tx_byte_buf = ""
        self.rx_byte_buf = ""
        super(Connection, self).__init__()
        self.name = "Connection"
        self.daemon = True

    def available(self):
        return len(self.rx_msg_buf)

    def flush_rx(self):
        self.rx_msg_buf = []

    def flush_tx(self):
        self.tx_msg_buf = []

    def get_message(self):
        msg = self.rx_msg_buf[0]
        self.rx_msg_buf = self.rx_msg_buf[1:]
        return msg

    def append_message(self, msg):
        self.tx_msg_buf.append(msg)

    def parse_rx(self):
        # XXX: This assumes that data comes in as a HEX formatted string,
        # and not e.g. a byte string. In message.py we make assumptions again.
        # Maybe this could be replaced by a regex searching for HEX strings
        # and a generic Message constructor, which decides based on the content which
        # message subclass to use. This function should have no knowledge of 
        # what message type this is.
        start = self.rx_byte_buf.rfind('CA55')
        if start > -1:
            if len(self.rx_byte_buf) - start > SensorMessage.BYTE_LENGTH*2:
                try:
                    msg = self.rx_byte_buf[start:start+SensorMessage.BYTE_LENGTH*2]
                    self.rx_byte_buf = ""
                    message = SensorMessage(msg)
                    if message.address is not None:
                        self.rx_msg_buf.append(message)
                except ValueError:
                    log_info("Message couldn't be parsed:")
                    log_info(msg)
        else:
            self.rx_byte_buf = ""

    def receive_bytes(self):
        """
        Overwrite this method. Should receive bytes from your datastream and
        append them to the rx_buffer.
        """
        pass

    def shutdown(self):
        self.running = False

    def send_bytes(self):
        """
        Overwrite this method. Should send bytes from the tx_buffer to your data
        stream
        """
        pass

    def run(self):
        while self.running:
            self.receive_bytes()
            self.parse_rx()
            # If messages have been enqueued, send over connection
            if len(self.tx_msg_buf) > 0:
                #print "Messages have been enqueued, trans to bytes"
                self.tx_byte_buf += self.tx_msg_buf[0].to_bytes()
                self.tx_msg_buf = self.tx_msg_buf[1:]
                self.send_bytes()
            time.sleep(.01)
        log_info(self.name + " done.")
