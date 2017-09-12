import serial
import Queue
import numpy as np
import struct
import threading 
import time
from sensortools.tools import log_message, log_info
import socket
import json


class SensorInterface(threading.Thread):
    """
    A thread that is used to enqueue outgoing messages and to pack and forward
    received messages via a callback
    """
    def __init__(self):
        ad = None
        log_info("SensorInterface init..")
        self.callbacks = []
        self.answers = {}
        self.connections = {}
        self.address_map = {}
        self.running = True
        threading.Thread.__init__(self)
        self.daemon = True

    def attach_connection(self, conn):
        if conn.name in self.connections:
            log_info("Connection has already been added, cancel..")
            return

        self.answers[conn.name] = []
        self.connections[conn.name] = conn
        conn.start()

    def drop_connections(self, conn):
        self.connections.pop(conn.name)
        self.answers.pop(conn.name)

    def register_callback(self, callback):
        """
        Register a function to receive a callback as soon as new data from 
        any sensor arrives. The method that registers for a callback last will be
        called first
        """
        log_info("Registering a new callback")
        self.callbacks.insert(0,callback)

    def unregister_callback(self, callback):
        log_info("Unregistered a new callback")
        self.callbacks.remove(callback)

    def shutdown(self):
        for conn in self.connections.values():
            conn.shutdown()
            conn.join()
        self.running = False

    def enqueue(self, message):
        if len(self.connections) == 0:
            log_info("No connections added yet, can't send message.")
        # In case there is only one connection, use that one.
        elif len(self.connections) == 1:
            self.answers[self.connections.keys()[0]].append(message)
            # In case there are multiple connections and we know from previous sensor messages
            # which one to use, choose the correct one.
        elif message.address in self.address_map:
            self.answers[self.address_map[message.address]].append(message)

        else:
            log_info("Don't know on which connection to send, dropping message..")


    def run(self):
        while self.running:
            for conn in self.connections.values():
                if conn.available():
                    msg = conn.get_message()
                    self.address_map[msg.address] = conn.name
                    #log_message(msg.to_bytes(), True, message_id=msg.message_id)
                    for callback in self.callbacks:
                        callback(msg)

                if len(self.answers[conn.name]) > 0:
                    conn.append_message(self.answers[conn.name][0])
                    #log_message(self.answers[conn.name][0].to_bytes()[5:], False, message_id=self.answers[conn.name][0].message_id);
                    self.answers[conn.name].pop(0)

            time.sleep(0.01)
        log_info("SensorInterface done.")



