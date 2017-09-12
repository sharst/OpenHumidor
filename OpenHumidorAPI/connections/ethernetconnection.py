#!/usr/bin/python
from connections.connection import Connection
from message import SensorMessage, BaseMessage
from sensortools.tools import log_info
import socket

class EthernetConnection(Connection):
    def __init__(self, is_server=True):
        super(EthernetConnection, self).__init__()
        self.port = 5000
        self.connected = False
        self.client_socket = None
        self.is_server = is_server
        self.server_socket = socket.socket()
        log_info("SerialConnection initialized.")

    def init_conn(self):
        while True:
            try:
                if self.is_server:
                    log_info(self.name + ": Trying to create a server at port " + repr(self.port))
                    self.createServer(self.port)
                    self.connected = True
                    return
                else:
                    log_info(self.name + ": Trying to connect to server at port " + repr(self.port))
                    self.createClient("localhost", self.port)
                    self.connected = True
                    return
            except socket.timeout:
                log_info(self.name + ": Timed out...")
            except:
                self.port += 1
                log_info(self.name + ": Increasing port number..")
                time.sleep(1)

    def createClient(self, address, port=5000):
        self.client_socket=socket.socket()
        print "Trying to connect.."
        self.client_socket.connect((address, port))
        self.client_socket.settimeout(1)
        print "Connected!"

    def createServer(self, port = 5000):
        self.server_socket.bind(("", port))
        socket.setdefaulttimeout(1)

        self.server_socket.listen(1)

        self.client_socket, address = self.server_socket.accept()

        if self.client_socket is not None:
            #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            #s.connect(('google.com', 0))

            log_info(self.name + ": Connected on ethernet!")
            #log_info(repr(s.getsockname()[0]))

    def receive_bytes(self):
        if not self.connected:
            self.init_conn()
            print "Init conn done."
        try:
            self.rx_byte_buf += self.client_socket.recv(1024)
            print "Received sth."
        except socket.timeout:
            print "Timed out"

    def send_bytes(self):
        print "In send_bytes"
        if not self.connected:
            self.init_conn()

        print "Sending bytes.."
        self.client_socket.send(self.tx_byte_buf)

    def shutdown(self):
        if self.server_socket is not None:
            self.server_socket.close()

        if self.client_socket is not None:
            self.client_socket.close()
