from cricketlib import searchswitch
from cricketlib import switch3141
import time

dev_list = searchswitch.get_switches()
print(dev_list)

swlist = dev_list["switches"]
for x in range(0, len(swlist)):
    if swlist[x]["model"] == "3141":
        cport = swlist[x]["port"]
        print("cport",cport)


    sw1 = switch3141.Switch3141(cport)
    sw1.connect()

    # Select the Switching the port Number
    port = 1
    port2 =2 

    sw1.port_on(port)
    time.sleep(1)
    sw1.port_off()

    # Select the Time Interval and duty
    interval = 2000
    duty = 30

    delayON = int(interval * duty / 100)
    delayOFF = int(interval * (100 - duty) / 100)

    delayStatement = "Auto Mode Start" +"   "+"Interval= "+str(interval)+"ms"+"   " +"duty= "+str(duty)+"%"+ "   " +"ON TIME:"+str(delayON)+"ms"+ "   " +"OFF TIME:"+str (delayOFF)+"ms"
    print(delayStatement)

    if dev_list['switches'][0]['model'] == '3141':
        while True:
            try:
                sw1.port_on(port)
                time.sleep(delayON/1000)
                port_on = "port"+ str(port)+"ON"
                print(port_on)
                
                sw1.port_off()
                port_on = "port"+ str(port)+"OFF"
                print(port_on)
                time.sleep(delayOFF/1000)

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
            


