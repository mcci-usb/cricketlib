##############################################################################
# 
# Module: loopmode.py
#
# Description:
#     This module provides a loop mode switching mechanism to automate 
#     the on and off states of a port based on given on time and off time durations. 
#     The on time represents the duration the port should be on, while the off time 
#     represents the duration the port should be off. This cycle repeats indefinitely.
#
# The below code refers only for MCCI Switch Model 3201, if using a different MCCI Switch Model
# kindly update the header accordingly.
# 
# Support MCCI Switch Models:
#     MCCI Switch Model 3141
#     MCCI Switch Model 3142
#     MCCI Switch Model 2301
#     MCCI Switch Model 2101
#
# Released under the MCCI Corporation.
#
##############################################################################
# including headers
# based on Model Switch update the header
# from cricketlib import switch3141

from cricketlib import searchswitch
from cricketlib import switch3201
import time

# Based on the Switch model, update the model name like "3142", "3141","2301" and "2101"
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
    #sw1 = switch3201.Switch3201(cport) 

    #Switch 3141 connected with comport 'COM<num>'
    sw1 = switch3201.Switch3201(cport)
    sw1.connect()   #Connect the Switch

    # Select the Switching the port Number
    port = 1  #Switching port 1 
    port2 =2  #Switching port 2

    # Select the Time Interval and duty
    OnTime = 3000  #Set ON time
    OffTime = 3000 #Set OFF time

    delayStatement = "Loop Mode Start" +"   " +"ON TIME:"+str(OnTime)+"ms"+ "   " +"OFF TIME:"+str (OffTime)+"ms"
    print(delayStatement)

    if dev_list['switches'][0]['model'] == '3141':
        while True:
            try:
                print("Port" + str(port)+ "ON")
                sw1.port_on(port)
                time.sleep(OnTime/1000)
                port_on = "port"+ str(port)+"ON"
                # print(port_on)
                
                print("Port" + str(port)+ "OFF")
                sw1.port_off()
                time.sleep(OffTime/1000)
                port_off = "port"+ str(port)+"OFF"
                
                #############################################################
                # Below code run port 2 switching.
                #############################################################

                # sw1.port_on(port2)
                # time.sleep(delayON/1000)
                # port_on = "port"+ str(port2)+"ON"
                # print(port_on)
                
                # sw1.port_off()
                # port_on = "port"+ str(port2)+"OFF"
                # print(port_on)
                # time.sleep(delayOFF/1000)
            
            except KeyboardInterrupt:
                print("Loop Mode Stopped")
                break

    else:
        print("Switch Model name not equal")