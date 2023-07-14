##############################################################################
# 
# Module: vbus_va.py
#
# Description:
#     the user can manually control the on and off states of the switch ports. 
#     It also includes functionality to read and update voltage and current measurements 
#     when switching the ports.
#
# The below code refers only for MCCI Switch Model 3201, if using a different 
# MCCI Switch Model kindly update the header accordingly.
# 
# Support MCCI Switch Models:
#     MCCI Switch Model 3201
#     MCCI Switch Model 3142
#     MCCI Switch Model 2301
# Released under the MCCI Corporation
#
##############################################################################
# avalaible list of MCCI Switches with port number
from cricketlib import searchswitch
from cricketlib import switch3201
import time

# Based on the Switch model, update the model name like "3142","2301"
# MCCI_Switch = "3141"
MCCI_Switch = "3201"

#printlist of MCCI Switches with Comport
dev_list = searchswitch.get_switches()
print(dev_list)

swlist = dev_list["switches"]
for x in range(0, len(swlist)):
    if swlist[x]["model"] == MCCI_Switch:
        cport = swlist[x]["port"]
        print("cport",cport)

#Based on the Switch connected change the below API
#sw1 = switch3201.Switch3141(cport)

sw1 = switch3201.Switch3201(cport)

sw1.connect() #Connect the Switch

time.sleep(1)  #set delay
sw1.port_on(1) #port 1 ON

volts = sw1.get_volts() # get the voltage reading switch 3201, 2301, 3142
print("volts:", volts)

amps = sw1.get_amps()  # get the Amps reading switch 3201, 2301, 3142
print("amps:", amps)

time.sleep(1) #set delay 1sec
sw1.port_off() #port off
sw1.get_volts()
sw1.get_amps()

time.sleep(1)
sw1.port_on(1)
volts = sw1.get_volts()
print("volts:", volts)
amps = sw1.get_amps()
print("amps:", amps)

time.sleep(1)
sw1.port_off()
sw1.get_volts()
print("volts:", volts)
sw1.get_amps()
print("amps:", amps)