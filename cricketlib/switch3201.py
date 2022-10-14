from cricketlib import switch 

class Switch3201(switch.Switch):
    def __init__(self, cport):
        switch.Switch.__init__(self, cport, 115200)
    
    def get_volts(self):
        cmd = 'volts\r\n'
        rc, rstr = self.send_cmd(cmd)
        print(rc, rstr)
        return (rc, rstr)

    def get_amps(self):
        cmd = 'amps\r\n'
        return self.send_cmd(cmd)