##############################################################################
# 
# Module: switch3201.py
#
# Description:
#     Top level API to manage USB Switch 3201
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

class Switch3201(switch.Switch):
    """
    Control class for Model 3201 switch.
    """
    def __init__(self, cport):
        switch.Switch.__init__(self, cport, 115200)
    
    def get_volts(self):
        """
        Reads voltage measurement.

        Returns :
            tuple : (status, voltage)
        """
        cmd = 'volts\r\n'
        rc, rstr = self.send_cmd(cmd)
        return (rc, rstr)

    def get_amps(self):
        """
        Reads current measurement.

        Returns :
            tuple : (status, current)
        """
        cmd = 'amps\r\n'
        return self.send_cmd(cmd)