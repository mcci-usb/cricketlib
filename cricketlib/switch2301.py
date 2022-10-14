from cricketlib import switch 

class Switch2301(switch.Switch):
    def __init__(self, cport):
        switch.Switch.__init__(self, cport, 9600)
    
    def get_volts(self):
        cmd = 'volts\r\n'
        return self.send_cmd(cmd)

    def get_amps(self):
        cmd = 'amps\r\n'
        return self.send_cmd(cmd)