import os
from os.path import join
import ipdb

def format_hex(msg):
    return "|".join(format(ord(x), "02x").upper() for x in msg)

def format_bytes(st):
    return "".join(st.split("|")[i].decode("hex") for i in range(len(st.split("|"))))

def shorten_number(num, places=2):
    return int(num*10**places)/float(10**places)

def find_tty_usb(idVendor, idProduct, busnum=None):
    """find_tty_usb('067b', '2302') -> '/dev/ttyUSB0'"""
    # Note: if searching for a lot of pairs, it would be much faster to search
    # for the enitre lot at once instead of going over all the usb devices
    # each time.
    for dnbase in os.listdir('/sys/bus/usb/devices'):
        dn = join('/sys/bus/usb/devices', dnbase)
        if not os.path.exists(join(dn, 'idVendor')):
            continue
        #print dn
        idv = open(join(dn, 'idVendor')).read().strip()
        if idv != idVendor:
            continue
        idp = open(join(dn, 'idProduct')).read().strip()
        if idp != idProduct:
            continue
        
        bus = open(join(dn, 'busnum')).read().strip()
        if busnum is not None:
            if busnum != int(bus):
                continue
            
        for subdir in os.listdir(dn):
            if subdir.startswith(dnbase + ':'):
                for subsubdir in os.listdir(join(dn, subdir)):
                    if subsubdir.startswith('ttyUSB'):
                        return join('/dev', subsubdir)
                    if subsubdir.startswith('tty'):
                        return join('/dev', os.listdir(join(dn, subdir, subsubdir))[0])

def find_serial_adapter(busnum=None):
    return find_tty_usb("067b", "2303", busnum=busnum)

def find_arduino_nano():
    return find_tty_usb("1a86", "7523")

def log_message(msg, incoming, sensid=None, maxlen=27, message_id=None):
    msg = format_hex(msg)
    msgs = [msg[i:i+maxlen] for i in xrange(0, len(msg), maxlen)]
    print("\t\t\t\t\t\t"),
    if not incoming:
        print("-->"),
    else:
        print("<--"),
        
    if sensid is not None:
        print(" " + repr(sensid)),
    
    if message_id is not None:
        print(" " + repr(message_id))
    print ": " 
    
    for msg in msgs:
        print ("\t\t\t\t\t\t" + msg)
    
    if not incoming:
        print "-"*60
        
def log_info(msg, maxlen = 40):
    msgs = [msg[i:i+maxlen] for i in xrange(0, len(msg), maxlen)]
    for msg in msgs:
        print msg
        
if __name__=="__main__":
    print "USB Adapter unten rechts"
    print find_serial_adapter(3)
    print "USB Adapter unten links"
    print find_serial_adapter(6)