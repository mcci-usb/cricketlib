# avalaible list of MCCI Switches with port number
from cricketlib import searchswitch
# import lib for switch 3142, switch3201, switch 2101, 2301
from cricketlib import switch3141
from cricketlib import switch3142
# from cricketlib import switch3201
# from cricketlib import switch2101 as S2101
# from cricketlib import switch2301
import time

# found a list of available switches.
# using the port number open the switch.
dev_list = searchswitch.get_switches()
print(dev_list)
# open switch 3141
sw1 = switch3141.Switch3141('COM6')
# Connect the USB Switch to particular port number.
# Connect the USB Switch
sw1.connect()
# port on command using parameters depends upon switches.
sw1.port_on(1)
# add delay to see the effect of port on.
time.sleep(1)
# Switching the port OFF
sw1.port_off()
# port on command using parameters depends upon switches.
sw1.port_on(2)
# add delay to see the effect of port on.
time.sleep(1)
# Switching the port OFF
sw1.port_off()
print("Model 3141 - Test completed successfully.")
sw2 = switch3141.Switch3141('COM11')
# Connect the USB Switch
sw2.connect()
# port on command using parameters depends upon switches.
sw2.port_on(1)
# add delay to see the effect of port on.
time.sleep(1)
# Switching the port OFF
sw2.port_off()
# port on command using parameters depends upon switches.
sw2.port_on(2)
# add delay to see the effect of port on.
time.sleep(1)
# Switching the port OFF
sw2.port_off()
print("Model 3142 - Test completed successfully.")