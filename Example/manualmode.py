##############################################################################
# 
# Module: manualmode.py
#
# Description:
#     This module provides a manual mode functionality for 
#     the MCCI Switch Models 3201, 3141, 2101, and 2301. 
#     In manual mode, the user can manually control 
#     the on and off states of the switch ports.
#
# The below code refers only for MCCI Switch Model 3201, if using a different MCCI Switch Model
# kindly update the header accordingly.
# 
# Support MCCI Switch Models:
#     MCCI Switch Model 3201
#     MCCI Switch Model 3142
#     MCCI Switch Model 2301
#     MCCI Switch Model 2101
#
# Released under the MCCI Corporation
#
##############################################################################

# avalaible list of MCCI Switches with port number
from cricketlib import searchswitch
from cricketlib import switch3141
import time

# Based on the Switch model, update the model name like "3142", "3201","2301" and "2101"
# MCCI_Switch = "3201"
MCCI_Switch = "3141"

delay = 1
#printlist of MCCI Switches with Comport
dev_list = searchswitch.get_switches()
print(dev_list)

# Serial Communication---
# windows Platform
# here COM5, COM8, COM13...etc are exapmple ports.
swlist = dev_list["switches"]
for x in range(0, len(swlist)):
    if swlist[x]["model"] == MCCI_Switch:
        cport = swlist[x]["port"]
        print("cport",cport)

#Based on the Switch connected change the below API
#sw1 = switch3201.Switch3201(cport) 

#Switch 3141 connected with comport 'COM<num>'
sw1 = switch3141.Switch3141(cport)
sw1.connect() #Connect the Switch

time.sleep(delay)  #set delay
sw1.port_on(1) #port 1 ON


sw1.port_off() #port 1 OFF
time.sleep(delay)  #set delay


time.sleep(1)
sw1.port_on(2) #port 2 ON

time.sleep(1)
sw1.port_off() #port 2 OFF