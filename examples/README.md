# example-cricketapi

This repo contains example python scripts that uses MCCI Python library [cricketlib](https://github.com/mcci-usb/cricketlib) to control MCCI USB Switches Model 3201, Model 3141, Model 2301, Model 2101, Model 3142

Before start using the example python scripts ensure to install the required libraries.
follow the readme file to install all required libraries

[cricketlib's READEME](https://github.com/mcci-usb/cricketlib#readme)

## example scripts

**Manual Mode**:

The `manualmode.py` module facilitates manual control of the switch ports for MCCI Switch Models 3141, 3201, 3142, 2101, and 2301. In this mode, the user can manually switch the ports on or off according to their requirements. Additionally, this module allows for voltage and current readings when switching the ports on. The switch_port_on function turns on the specified port, reads the voltage and current measurements, and returns them as output. On the other hand, the switch_port_off function simply turns off the specified port. Users can integrate this module into their own applications or scripts to enable interactive control and monitoring of the switch ports.

**Auto Mode**:

The `automode.py` module provides a flexible switching mechanism to automate the on and off states of a port based on a given duty cycle and interval. This module supports various MCCI Switch Models, including the MCCI Switch Model 3141, 3142, 3201, 2301, and 2101. By specifying the duty cycle as a percentage and the interval duration, the module handles the automatic switching of the port on and off. It ensures that the port is turned on for the specified proportion of time within the interval, and the cycle repeats accordingly.

**Loop Mode**:

In the `loopmode.py` module, loop mode is implemented, allowing the user to control the on and off states of a port based on specific on time and off time durations. This module is also compatible with MCCI Switch Models 3141, 3142, 3201, 2301, and 2101. Once the on time and off time durations are provided, the module runs an infinite loop where the port is turned on for the specified on time duration and then turned off for the specified off time duration. This looping cycle continues indefinitely until the program is interrupted.

**VBus Monitor**:

In the `vbus_va.py` the user can manually control the on and off states of the switch ports. It also includes functionality to read and update voltage and current measurements when switching the ports.

## Library & APIs description

This section describes about the main library and APIs of cricketlib

### How to search available MCCI switches

This library `searchswitch` is responsible fetching available MCCI switches connected to the host machine.

```python
# avalaible list of MCCI Switches with port number
from cricketlib import searchswitch
```

```python
# found a list of available switches.
# using the port number open the switch.
dev_list = searchswitch.get_switches()
```

### How to connect the MCCI Switch to a particular Port number

```python
# import lib for switch 3142, 3201, 2101, 2301
# based on the Switch used update the import lib.
# sample: from cricketlib import switchXXXX

# here 3141 is used, and importing resp. library
from cricketlib import switch3141
# from cricketlib import switch3201
# from cricketlib import switch2101 as S2101
# from cricketlib import switch2301
# from cricketlib import switch3142
```

```python
# --- Windows Platform ---
# here COM5, COM8, COM13...etc are example ports.
# Based on the Switch connected, change the below API with the resp. COM Port
# sample: sw1 = switchXXXX.SwitchXXXX('COMX')

sw1 = switch3201.Switch3201('COM5') 

# sw1 = switch3141.Switch3141('COM8')
# sw1 = S2101.Switch2101('0002CC0014FF')
# sw1 = switch2301.Switch2301('COM13')
```

**NOTE**: Switch 2101 is an HID device and can't be opened via COM PORT, rather it can be opened via it's serial number.

```python
# --- Linux Platform ---
# here /dev/ttyACMO, /dev/ttyACM1, etc are example port handles.
# Based on the Switch connected, change the below API with the device handle
# sample: sw1 = switchXXXX.SwitchXXXX('/dev/ttyXXXX')

sw1 = switch3201.Switch3201('/dev/ttyACMO')

# sw1 = switch3141.Switch3141('/dev/ttyACMO')
# sw1 = switch2301.Switch2301('/dev/ttyACM1')
```

`connect()` is the switch API to connect the switch to the Host machine via the port/handle.

``` python
# Connect the USB Switch
sw1.connect()
```

### Port ON/OFF Commands

#### Switching the port ON

```python
# Port ON with port number
# sw1.port_on(1) first port ON
# sw1.port_on(2) second port ON
# sw1.port_on(3) third port 
# sw1.port_on(4) fourth port ON

# The switch3201, switch2301 is equipped with 4 ports for testing/communicating with the DUTs
# for switch3141, switch3142 is equipped with 2 ports for testing/communicating with the DUTs
# for switch2101 is equipped with only 1 port for testing/communicating with the DUT

sw1.port_on(1)
```

#### Switching the port OFF

```python
# Port OFF with port number default empty or 0.
sw1.port_off()
```

## Get/Set Commands

### Get Status

Gets the status of current port number.

```python
sw1.get_status()
```

### Get Voltage Readings

Gets the Voltage reading (supprts only for switches 3201, 2301 & 3142)

```python
sw1.get_volts()
```

### Get Current Readings

Gets the Current reading (supprts only for switches 3201, 2301 & 3142)

```python
sw1.get_amps()
```

### Set Speed

Switch API to set the desired speed (supported speeds are HS & SS).

```python
# Set High Speed
sw1.set_speed("HS")
# Set Super Speed
sw1.set_speed("SS")
```

## How to use a Switch to enumerate in different speeds

Below code describes how a switch (here we have used 2101) can be used to enumerate on both superspeed and highspeed.

```python
from cricketlib import switch2101


# Connecting the 2101 switch
switch = Switch2101.Switch2101('0002CC0014FF')
switch.connect()
# Turning the Port with SuperSpeed
switch.port_on("ss")
time.sleep(2)
# Turning the Port OFF
switch.port_off()
time.sleep(1)
# Turning the Port with HighSpeed
switch.port_on("hs")
time.sleep(1)
# Turning the Port OFF
switch.port_off()
```
