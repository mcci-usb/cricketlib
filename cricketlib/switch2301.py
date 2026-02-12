##############################################################################
# 
# Module: switch2301.py
#
# Description :
#     High-level API for USB Switch Model 2301.
#
#     Provides voltage and current monitoring
#     along with standard switch control operations.
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

class Switch2301(switch.Switch):
    """
    Control class for Model 2301 Serial Switch.

    Parameters :
        cport (str) : COM port name
    """
    
    def __init__(self, cport):
        switch.Switch.__init__(self, cport, 9600)
    
    def get_volts(self):
        """
        Reads voltage measurement.

        Returns :
            tuple : (status, voltage_string)
        """
        cmd = 'volts\r\n'
        return self.send_cmd(cmd)

    def get_amps(self):
        """
        Reads current measurement.

        Returns :
            tuple : (status, current_string)
        """
        
        cmd = 'amps\r\n'
        cmd = 'amps\r\n'
        return self.send_cmd(cmd)