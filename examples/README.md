# cricketlib

This is a Python library to control MCCI USB Switches Model 3201, Model 3141, Model 2301, Model 2101, Model 3142

Before start the this test file ensure need To install the required libraries.
Visit the following link [READEME](https://github.com/mcci-usb/cricketlib#readme)

follow the readme file to install all required libraries from here 

```python
# avalaible list of MCCI Switches with port number
from cricketlib import searchswitch
```
```python
# import lib for switch 3142, switch3201, switch 2101, 2301
# based on the Switch mode update the import lib.
from cricketlib import switch3141
#from cricketlib import switch3201
#from cricketlib import switch2101 as S2101
#from cricketlib import switch2301
#from cricketlib import switch3142
```
```python
# found a list of available switches.
# using the port number open the switch.
dev_list = searchswitch.get_switches()
print(dev_list)
```
```python
# Serial Communication---
# windows Platform
# here COM5, COM8, COM13...etc are exapmple ports.
#Based on the Switch connected, change the below API with Comport
#sw1 = switch3201.Switch3141('COMX')

sw1 = switch3201.Switch3201('COM5') 
# sw1 = switch3141.Switch3141('COM8')
# sw1 = switch2101.Switch2101('0002CC0014FF')
# sw1 = switch2301.Switch2301('COM13')
```
```python
# ---Linux Platform Serial Communication---
# here /dev/ttyACMO, /dev/ttyACMO.etc are exapmple ports number.
#Based on the Switch connected, change the below API with Comport
#sw1 = switch3201.Switch3141('/dev/ttyACMO')
sw1 = switch3201.Switch3201('/dev/ttyACMO')
# sw1 = switch3141.Switch3141('/dev/ttyACMO')
```
### Connect the USB Switch to particular port number.
``` python
# Connect the USB Switch
sw1.connect()
```
### port on command using parameters depends upon switches
```python
# port on with port number
# sw1.port_on(1) first port ON
# sw1.port_on(2) second port ON
# sw1.port_on(3) third port 
# sw1.port_on(4) fourth port ON
# for switch3201, switch2301 have 4 ports
# for switch3141, switch3142 have 2 ports
# for switch2101 have 1 port

sw1.port_on(1)
```
### Switching the port OFF
```python
# port off with port number default empty or 0.
sw1.port_off()
```
### Requested commands

### Set Speed information 
```python
# Set High Speed
sw1.set_speed("HS")
# Set Super Speed
sw1.set_speed("SS")
```
### Get Status
```python
# Get the status of current port number.
sw1.get_status()
```
### Get the Volts and Amps information
```python
# get the voltage reading only for switch 3201, switch2301 and Switch3142
sw1.get_volts()
# get the amps reading only for switch 3201, switch2301 and switch3142
sw1.get_amps()
```
### Switch 2101 ports switching
```
sw3 = S2101.Switch2101('0002CC0014FF')
sw3.connect()
sw3.port_on("ss")
time.sleep(2)
sw3.port_off()
time.sleep(1)
sw3.port_on("hs")
time.sleep(1)
sw3.port_off()
```