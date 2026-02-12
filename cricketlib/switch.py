##############################################################################
# 
# Module: switch.py
#
# Description :
#     High-level switch control APIs
#     for Serial-based MCCI Switches.
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
#   V1.0.8 Thu Feb 2026 12:05:00   Vinay N
#       Module created
##############################################################################

from cricketlib import serialswitch

class Switch(serialswitch.SerialDev):
    """
    Provides switch control operations.

    Features :
        • Connect / Disconnect
        • Port ON / OFF
        • Status monitoring
        • Speed configuration
    """
    def __init__(self, cport, baud):
        """
        Initializes switch instance.

        Parameters :
            cport (str) : COM port
            baud (int) : Baud rate
        """
        self.sport = serialswitch.SerialDev(cport, baud)
    
    def connect(self):
        """Establish device connection."""
        
        return self.sport.open()

    def disconnect(self):
        """Close device connection."""
         
        return self.sport.close()

    def port_on(self, pno):
        """
        Turns ON specified port.

        Parameters :
            pno (int) : Port number
        """
        
        cmd = self.port_cmd(pno)
        return self.send_cmd(cmd)

    def port_off(self):
        """Turns OFF all ports."""
         
        cmd = self.port_cmd(0)
        return self.send_cmd(cmd)

    def get_port_status(self):
        """Reads port status."""
        
        cmd = 'port\r\n'
        return self.send_cmd(cmd)

    def get_version(self):
        """Reads firmware version."""
         
        cmd = 'version\r\n'
        return self.send_cmd(cmd)

    def send_cmd(self, cmd):
        """
        Sends command and reads response.

        Returns :
            tuple : (status, response)
        """
        
        res = self.sport.write(cmd)
        if res > 0:
            res, rstr = self.sport.read()
        else:
            rstr = "Comm Error\n"
        return res, rstr
    
    def send_reset(self, cmd):
        """
        Sends reset command.

        Returns :
            tuple : (status, message)
        """
        
        res = self.sport.write(cmd)
        if res > 0:
            rstr = "success\n"
        else:
            rstr = "Comm Error\n"
        return res, rstr

    def port_cmd(self, pno):
        """Builds port command string."""
        
        return 'port '+str(pno)+'\r\n'

    def set_speed(self, speed):
        """
        Configures USB speed.

        Parameters :
            speed (str) : 'SS' for SuperSpeed

        Returns :
            tuple : (status, response)
        """
        
        if speed == "SS":
            val = 1
        else:
            val = 0
        cmd = 'superspeed'+' '+str(val)+'\r\n'
        res, outstr = self.send_cmd(cmd)
        if res == 0:
            outstr = outstr.replace('s', 'S')
            outstr = outstr.replace('1', 'Enabled')
            outstr = outstr.replace('0', 'Disabled')
        return res, outstr

    def send_status_cmd(self, cmd):
        """
        Sends long status command.

        Reads multiple response lines.

        Returns :
            tuple : (status, full_response)
        """
        
        outstr = ""
        res = self.sport.write(cmd)
        if res > 0:
            for i in range(25):
                res, rstr = self.sport.read()
                if res == 0:
                    outstr = outstr + rstr
        elif res == 0:
            outstr = "Comm Error\n"
        return res, outstr