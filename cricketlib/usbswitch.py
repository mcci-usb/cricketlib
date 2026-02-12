##############################################################################
# 
# Module: usbswitch.py
#
# Description:
#     API to manage USB Switch 2101
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

import hid

VID_2101 = 0x040e
PID_2101 = 0xf413

class UsbSwitch:
    """
    HID communication handler for Model 2101.

    Parameters :
        slno (str) : Device serial number
    """
    def __init__(self, slno):
        self.slno_list = []
        self.path_list = []
        self.dev_list = []
        self.slno = slno
        self.path = None
        self.dev = None
        self.ready = False

    def get_2101(self):
        """
        Enumerates connected 2101 devices.

        Returns :
            list[str] : Serial numbers
        """
        dlist = []
        dev = hid.enumerate(VID_2101, PID_2101)
        if len(dev) != 0:
            for dev in hid.enumerate(VID_2101, PID_2101):
                dlist.append(dev['serial_number'])

        return dlist

    def scan_2101(self):
        """
        Scans and stores device paths.

        Returns :
            list[str] : Serial numbers detected
        """
        dlist = []
        self.slno_list.clear()
        
        self.path_list.clear()
    
        dev = hid.enumerate(VID_2101, PID_2101)
        if len(dev) != 0:
            for dev in hid.enumerate(VID_2101, PID_2101):
                try:
                    dlist.append(dev['serial_number'])
                    self.slno_list.append(dev['serial_number'])
                    self.path_list.append(dev['path'])
                except:
                    print("Path Error")
        
        self.ready = True
        return dlist

    def select_usb_switch(self, serialno):
        """
        Selects device by serial number.

        Parameters :
            serialno (str)

        Returns :
            bool : True if found
        """
        self.slno = None
        self.path = None
        
        for i in range(len(self.slno_list)):
            if(self.slno_list[i] == serialno):
                self.slno = serialno
                self.path = self.path_list[i]
                break
            
        if self.slno == serialno:
            return True
        else:
            return 
    
    def read_status(self):
        """
        Reads port status via HID input report.

        Returns :
            tuple : (status, raw_bytes)
        """
        result = None
        res = -1

        dev = hid.device()
        dev.open_path(self.path)
        result = dev.get_input_report(0x00, 0x03)
        dev.close()
        res = 0
        
        return res, result

    def control_port(self, cmd):
        """
        Sends control command via HID.

        Parameters :
            cmd (int) : Control word

        Returns :
            tuple : (status, bytes_written)
        """
        result = None
        res = -1

        dev = hid.device()
        dev.open_path(self.path)
        result = dev.write([0x00, cmd])
        dev.close()
        res = 0
    
        return res, result