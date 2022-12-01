##############################################################################
# 
# Module: searchswitch.py
#
# Description:
#     API to show list of available MCCI USB Switch (3141, 3201, 2101 and 2301)
#
# Copyright notice:
#     This file copyright (c) 2022 by
#
#         MCCI Corporation
#         3520 Krums Corners Road
#         Ithaca, NY  14850
#
#     Released under the MCCI Corporation.
#
# Author:
#     Seenivasan V, MCCI Corporation Dec 2022
#
# Revision history:
#    V1.0.4 Thu Dec 01 2022 12:05:00   Seenivasan V
#       Module created
##############################################################################
# Lib imports

import sys
import serial
import serial.tools.list_ports
import time
import sys
import usb.util
from usb.backend import libusb1
import platform

if sys.platform == 'darwin':
    import hid

VID_2101 = 0x040e
PID_2101 = 0xf413

path = sys.executable
path = path.replace("python.exe", "")

if sys.platform == 'win32':
        pver = platform.architecture()
        if pver[0] == '64bit':
            usb.backend.libusb1.get_backend(find_library=lambda x: "" + 
            path + "Lib\\site-packages\\libusb\\_platform\\_windows\\x64\\libusb-1.0.dll")
            print("64bit NBA")
        else:
            usb.backend.libusb1.get_backend(find_library=lambda x: "" + 
            path + "Lib\\site-packages\\libusb\\_platform\\_windows\\x86\\libusb-1.0.dll")
            print("32bit NBA")


def version():
    return "Cricketlib v1.0.4"

def get_switches():
    devList = search_switches()
    return devList

def filter_port():
    usb_hwid_str = ["USB VID:PID=045E:0646", "USB VID:PID=2341:0042"]
    comlist = serial.tools.list_ports.comports()
    port_name = []

    for port, desc, hwid in sorted(comlist):
        res = [True for gnhwid in usb_hwid_str if(gnhwid in hwid)]
        if(res):
            port_name.append(port)
    return port_name

def get_2101():
    """
    get the model2101 enumaration in darwin 
    Args:
        self: The self parameter is a reference to the current 
        instance of the class,and is used to access variables
        that belongs to the class.
    Returns: 
        dlist: return same device model
    """
    dlist = []
    if sys.platform == 'darwin':
        dev = hid.enumerate(VID_2101, PID_2101)
        if len(dev) != 0:
            for dev in hid.enumerate(VID_2101, PID_2101):
                dlist.append(dev['serial_number'])
    else:
        for dev in usb.core.find(idVendor=VID_2101, idProduct=PID_2101, 
                                    find_all=1):
            slno =  get_serial_number(dev)
            dlist.append(slno)
    return dlist

def get_serial_number(dev):
    """
    Get Serial number of the model 2101 device

    Args:
        dev: 2101 device found in the USB bus 
    Returns:
        serial number of the device in String format
    """
    ret  = None

    try:
        ret = dev.ctrl_transfer(0x80, 0x06, 0x303, 0x409, 0x1a)
    except:
        ret = None

    # Create data buffers
    intarr = []
    # Length of array in integer
    alen = int(len(ret)/2) - 1
    k = 2
    
    for i in range(alen):
        byt = [ret[k], ret[k+1]]
        intpack = int.from_bytes(byt, byteorder='little')
        intarr.append(intpack)
        k = k + 2
    
    slno = "".join(map(chr, intarr))
    return slno

def search_switches():
    port_name = []
    rev_list = []
    dev_list = []

    # Get list of 3141, 3201, 2301 switches    
    port_name = filter_port()

    for i in range(len(port_name)):
        try:
            ser = serial.Serial(port=port_name[i], baudrate=115200, 
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE, timeout=1, 
                                stopbits=serial.STOPBITS_ONE)
           
            time.sleep(1)
    
            cmd = 'version\r\n'
            ser.write(cmd.encode())
            strout = ser.readline().decode('utf-8')
            nstr = strout[2:]
            if(nstr.find('01') != -1):
                rev_list.append(port_name[i])
                dev_list.append('3141')
            elif(nstr.find('12') != -1):

                rev_list.append(port_name[i])
                dev_list.append('3201')
            ser.close()

            # Here the baudrate as fixed the 9600 
            # baudrate supports Model 2301 device
            ser = serial.Serial(port=port_name[i], baudrate=9600, 
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE, timeout=1, 
                                stopbits=serial.STOPBITS_ONE)
            time.sleep(1)
    
            cmd = 'version\r\n'
    
            ser.write(cmd.encode())
            strout = ser.readline().decode('utf-8')
            nstr = strout[2:]
            if(nstr.find('08') != -1):
                rev_list.append(port_name[i])
                dev_list.append('2301')
            ser.close()

        except serial.SerialException as e:
            pass

    # Get the list of 2101
    dlist = get_2101()

    for dl in dlist:
        rev_list.append(dl)
        dev_list.append('2101')
        
    rdict = {}
    devlist = []
    
    for i in range(len(rev_list)):
        tempdict = {}
        tempdict["port"] = rev_list[i]
        tempdict["model"] = dev_list[i]
        devlist.append(tempdict)

    rdict["switches"] = devlist
    return rdict