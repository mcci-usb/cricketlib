##############################################################################
# 
# Module: automode.py
#
# Description:
#     This module provides a flexible switching mechanism to automate 
#     the on and off states of a port based on a given duty cycle and interval. 
#     The duty cycle represents the proportion of time the port should be on within 
#     the interval and is expressed as a percentage. 
#     The interval refers to the total duration of one cycle, 
#     including both the on and off states of the port.
#
# The below code refers only for MCCI Switch Model 3141, if using a diffrent MCCI Switch Model
# kindly update the header accordingly.
# 
# Support MCCI Switch Models:
#     MCCI Switch Model 3142
#     MCCI Switch Model 3201
#     MCCI Switch Model 2301
#     MCCI Switch Model 2101
#
# Released under the MCCI Corporation.
#
##############################################################################
# including headers
# based on Model Switch update the header
# from cricketlib import switch3201

from cricketlib import searchswitch
from cricketlib import switch3141
import time

# Based on the Switch model, update the model name like "3142", "3201","2301" and "2101"
# MCCI_Switch = "3201"
MCCI_Switch = "3141"

#print list of MCCI Switches with Comport
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
    sw1 = switch3141.Switch3141(cport)
    sw1.connect()  #Connect the Switch

    # Select the Switching the port Number
    port = 1
    port2 =2 
  
    interval = 9000  #Slect the Interval
    duty = 30        #Select the Duty Cycle

    delayON = int(interval * duty / 100)           #delay ON time
    delayOFF = int(interval * (100 - duty) / 100)  #delay OFF time

    delayStatement = "Auto Mode Start" +"   "+"Interval= "+str(interval)+"ms"+"   " +"duty= "+str(duty)+"%"+ "   " +"ON TIME:"+str(delayON)+"ms"+ "   " +"OFF TIME:"+str (delayOFF)+"ms"
    print(delayStatement)

    if dev_list['switches'][0]['model'] == '3141':
        while True:
            try:
                print("Port" + str(port)+ "ON")
                sw1.port_on(port)
                time.sleep(delayON/1000)
                port_on = "port"+ str(port)+"ON"
                
                print("Port" + str(port)+ "OFF")
                sw1.port_off()
                time.sleep(delayON/1000)
                port_on = "port"+ str(port)+"OFF"


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
                print("Auto Mode Stopped")
                break

    else:
        print("Switch Model name not equal")