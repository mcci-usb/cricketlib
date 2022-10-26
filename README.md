# cricketlib

This is a Python library to control MCCI USB Switches.

### Install Python package
install python package from [python.org](https://www.python.org/ftp/python/3.7.8/python-3.7.8.exe)

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

### libusb-1.0.dll Library

```python
If on 64-bit Windows, copy libusb-1.0.dll library into C:\windows\SysWOW64
```

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
sw2 = switch3141.Switch3141('COM8')
(or)
sw3 = switch2101.Switch2101('0A88C1001416')
(or)
sw4 = switch2301.Switch2301('COM13')
```
```python
# ---Serial Communication---
#Linux Platform
# here /dev/ttyUSB0, /dev/ttyUSB1.etc are exapmple ports.
sw1 = switch3201.Switch3201('/dev/ttyUSB0') 
(or)
sw2 = switch3141.Switch3141('/dev/ttyUSB1')
```
### Connect the USB Port
``` python
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

## Release History
- v1.0.1 update speed change in switch2101
- v1.0.0 initial release.







