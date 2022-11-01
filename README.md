# cricketlib

This is a Python library to control MCCI USB Switches.

### Install Python3.7 (32-bit) package 
install python package from [python.org](https://www.python.org/ftp/python/3.7.8/python-3.7.8.exe)


### Install Python3.7 (64-bit) package
install python package from [python.org](https://www.python.org/ftp/python/3.7.8/python-3.7.8-amd64.exe)

### Install pip package
```shell
pip --version
python -m pip install --upgrade pip
```

### Prerequisites for running or building

<strong>On Windows:</strong>

Development environment

* OS - Windows 10 and 11 64 bit
* Python - 3.7.8
* pyserial - 3.5
* pyusb - 1.2.1
* libusb - 1.0.24b3
* libusb1 - 3.0.0

```shell
pip install pyserial
pip install pyusb
pip install libusb
pip install libusb1
```
# pyusb Error

### Installing Python Packages with Setup.py

1.  Clone the repository from [github](https://github.com/mcci-usb/cricketlib)

2.  Open a terminal window and change directory to  `{path_to_repository}/cricketlib`. using `cd` into the root directory where setup.py is located

3.  To install the library in your local Python setup, enter the command
```bash
python setup.py install
```

Please navigate to dist/ directory and you will find the files .egg file.
Example: `cricketapi-1.0.0-py3.7.egg`

## How to use the package
Create a Python file and import the class library from package:

```python
from cricketlib import searchswitch
from cricketlib import switch3141
from cricketlib import switch3201
from cricketlib import switch2101 as S2101
from cricketlib import switch2301
```
```python
# --- found a list of available switches
dlist = searchswitch.get_switches()
```
```python
# ---Serial Communication---
# windows Platform
# here COM5, COM8, COM13...etc are exapmple ports.
sw1 = switch3201.Switch3201('COM5') 
(or)
sw1 = switch3141.Switch3141('COM8')
(or)
sw1 = switch2101.Switch2101('0002CC0014FF')
(or)
sw1 = switch2301.Switch2301('COM13')
```
```python
# ---Serial Communication---
#Linux Platform
# here /dev/ttyACMO, /dev/ttyACMO.etc are exapmple ports.
sw1 = switch3201.Switch3201('/dev/ttyACMO') 
(or)
sw1 = switch3141.Switch3141('/dev/ttyACMO')
```
### Connect the USB Port
``` python
# Connect the USB Switch
sw1.connect()
```
### Switching the port ON
```python
# --- port on with port number
sw1.port_on(1)
```
### Switching the port OFF
```python
# --- port off with port number default empty or 0.
sw1.port_off()
```
### Requested commands

### Set Speed
```python
# --- High Speed
sw1.set_speed("HS")
# --- Super Speed
sw1.set_speed("SS")
```
### Get Status
```python
# --- Get the Current port status
sw1.get_status()
```

### Get Volt Switch3201 and Switch2301
```python
# --- get the voltage only for switch 3201, switch2301
sw1.get_volts()
# --- get the amps only for switch 3201, switch2301
sw1.get_amps()
```
### Switch 2101 ports switching
```
sw3 = S2101.Switch2101('0002CC0014FF')
sw3.port_on("ss")
time.sleep(2)
sw3.port_off()
time.sleep(1)
sw3.port_on("hs")
time.sleep(1)
sw3.port_off()
```

## Release History
- v1.0.3 Support python 64-bit
- v1.0.2 update speed change in switch2101
- v1.0.0 initial release