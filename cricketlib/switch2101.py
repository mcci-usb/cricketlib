from cricketlib import usbswitch

##############################################################################
# 2101 Control Words
##############################################################################
CHECK_STATUS    = 0x00
DEV_RESET       = 0x01
DEV_VERSION     = 0x02
HS_CONNECT      = 0x03
DEV_CUSTOM      = 0x04
SS_CONNECT      = 0x05
DEV_DISCONNECT  = 0x06

class Switch2101(usbswitch.UsbSwitch):
    def __init__(self, slno):
        self.slno = slno
        self.portcmd = SS_CONNECT
        self.usbnode = usbswitch.UsbSwitch(slno)
    
    def connect(self):
        self.usbnode.scan_2101()
        self.usbnode.select_usb_switch(self.slno)

    def port_on(self, speed):
        if speed.lower() == "ss":
            self.portcmd = SS_CONNECT
        else:
            self.portcmd = HS_CONNECT
        rc, rs = self.usbnode.control_port(self.portcmd)
        return rc, rs
    
    def port_off(self):
        rc, rs = self.usbnode.control_port(DEV_DISCONNECT)
        return rc, rs