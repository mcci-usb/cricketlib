import serial
import serial.tools.list_ports

class SerialDev:
    def __init__(self, port, baud):
        self.handler = None
        self.port = port
        self.baud = baud

    def open(self):
        self.handler = serial.Serial()
        self.handler.port = self.port
        self.handler.baudrate = self.baud
        self.handler.bytesize = serial.EIGHTBITS
        self.handler.parity = serial.PARITY_NONE
        self.handler.timeout = 1
        self.handler.stopbits =serial. STOPBITS_ONE
        
        try:
            res = self.handler.open()
            return True
        except serial.SerialException as e:
            return False
            
    def close(self):
        try:
            self.handler.close()
            return True
        except:
            return False

    def write(self, cmd):
        try:
            cnt = self.handler.write(cmd.encode())
            return cnt
        except:
            return -1

    def read(self):
        try:
            return  0, self.handler.readline().decode('utf-8')
        except:
            return -1