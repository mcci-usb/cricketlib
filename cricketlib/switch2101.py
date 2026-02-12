##############################################################################
# 
# Module: switch2101.py
#
# Description :
#     High-level control API for USB Switch Model 2101.
#
#     This module provides control operations over HID interface
#     for managing USB data path connection/disconnection and
#     port speed configuration.
#
# Copyright notice:
#     This file copyright (c) 2026 by
#
#         MCCI Corporation
#         3520 Krums Corners Road
#         Ithaca, NY  14850
#
#     Released under the MCCI Corporation.
#
# Author:
#     Vinay N, MCCI Corporation Feb 2026
#
# Revision history:
#    V1.0.8 Thu Feb 2026 12:05:00   Vinay N
#       Module created
##############################################################################

from cricketlib import usbswitch

##############################################################################
# 2101 Control Words
##############################################################################
CHECK_STATUS    = 0x00
DEV_RESET       = 0x01
DEV_VERSION     = 0x02
HS_CONNECT      = 0x03
DEV_CUSTOM      = 0x04
SS_CONNECT      = 0x05
DEV_DISCONNECT  = 0x06

class Switch2101(usbswitch.UsbSwitch):
    """
    USB HID based control class for Model 2101 switch.

    Parameters :
        slno (str) : Device serial number
    """
    
    def __init__(self, slno):
        self.slno = slno
        self.portcmd = SS_CONNECT
        self.usbnode = usbswitch.UsbSwitch(slno)
    
    def connect(self):
        """
        Connects to the USB switch device.

        Returns :
            None
        """
        self.usbnode.scan_2101()
        self.usbnode.select_usb_switch(self.slno)

    def read_port(self):
        """
        Reads current port status.

        Returns :
            tuple :
                (status_code, raw_status_bytes)
        """
        rc, rs = self.usbnode.read_status()
        return rc, rs

    def port_on(self, speed):
        """
        Enables USB connection.

        Parameters :
            speed (str) :
                'SS' → SuperSpeed
                'HS' → HighSpeed

        Returns :
            tuple : (status, response)
        """
        
        if speed.lower() == "ss":
            self.portcmd = SS_CONNECT
        else:
            self.portcmd = HS_CONNECT
        rc, rs = self.usbnode.control_port(self.portcmd)
        return rc, rs
    
    def port_off(self):
        """
        Disconnects USB data path.

        Returns :
            tuple : (status, response)
        """
        
        rc, rs = self.usbnode.control_port(DEV_DISCONNECT)
        return rc, rs