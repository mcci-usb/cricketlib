##############################################################################
# 
# Module: Serialswitch.py
#
# Description :
#     Serial communication abstraction layer
#     for MCCI Switch devices.
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
import serial
import serial.tools.list_ports

class SerialDev:
    """
    Handles low-level serial communication.

    Parameters :
        port (str) : COM port name
        baud (int) : Baud rate
    """
    def __init__(self, port, baud):
        self.handler = None
        self.port = port
        self.baud = baud

    def open(self):
        """
        Opens serial connection.

        Returns :
            bool : True if success
        """
        self.handler = serial.Serial()
        self.handler.port = self.port
        self.handler.baudrate = self.baud
        self.handler.bytesize = serial.EIGHTBITS
        self.handler.parity = serial.PARITY_NONE
        self.handler.timeout = 1
        self.handler.stopbits =serial. STOPBITS_ONE
        
        try:
            res = self.handler.open()
            return True
        except serial.SerialException as e:
            return False
            
    def close(self):
        """
        Closes serial connection.

        Returns :
            bool : Operation status
        """
        try:
            self.handler.close()
            return True
        except:
            return False

    def write(self, cmd):
        """
        Sends command to device.

        Parameters :
            cmd (str) : Command string

        Returns :
            int : Bytes written / -1 on error
        """
        try:
            cnt = self.handler.write(cmd.encode())
            return cnt
        except:
            return -1

    def read(self):
        """
        Reads device response.

        Returns :
            tuple :
                (status, response_string)
        """
        try:
            return  0, self.handler.readline().decode('utf-8')
        except:
            return -1