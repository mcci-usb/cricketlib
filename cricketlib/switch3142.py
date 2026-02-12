##############################################################################
# 
# Module: switch3141.py
#
# Description :
#     Control API for USB Switch Model 3142.
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

from cricketlib import switch 

class Switch3142(switch.Switch):
    """
    Control class for Model 3142 switch.
    """
    def __init__(self, cport):
        switch.Switch.__init__(self, cport, 115200)
    
    def get_status(self):
        """
        Retrieves device status.

        Returns :
            tuple : (status, status_string)
        """
        cmd = 'status\r\n'
        rc, rstr = self.send_status_cmd(cmd) 
        return(rc, rstr)
    
    def get_volts(self):
        """
        Reads voltage value.

        Returns :
            tuple : (status, voltage_string)
        """
        cmd = 'volts\r\n'
        rc, rstr = self.send_cmd(cmd)
        return (rc, rstr)

    def get_amps(self):
        """
        Reads current value.

        Returns :
            tuple : (status, current_string)
        """
        cmd = 'amps\r\n'
        rc, rstr = self.send_cmd(cmd)
        return (rc, rstr)
        # return self.send_cmd(cmd)

    def get_orientation(self):
        """
        Detects cable orientation.

        Returns :
            tuple : (status, orientation)
        """
        strin = "--"
        rc, rstr = self.get_status()
        if rc == 0:
            outstr = rstr.split('\n')
            cc1detect = None
            cc1led = None
            for instr in outstr:
                if 'CC1 detect:' in instr:
                    fstr = instr.split('0x')
                    cc1detect = int(fstr[1], 16)
                elif 'CC1 led:' in instr:
                    lstr = instr.split(':')
                    cc1led = int(lstr[1])
                    break
            if cc1led == 0 and cc1detect < 20:
                    strin = "Flip"
            elif cc1led == 1 and cc1detect > 20:
                strin = "Normal"
            return (rc, strin)
        else:
            return (rc, "ComError")
    
    def do_reset(self):
        """
        Resets the device.

        Returns :
            tuple : (status, message)
        """
        cmd = 'reset\r\n'
        rc, rstr = self.send_reset(cmd) 
        return(rc, rstr)
