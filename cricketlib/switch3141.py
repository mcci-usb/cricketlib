from cricketlib import switch 

class Switch3141(switch.Switch):
    def __init__(self, cport):
        switch.Switch.__init__(self, cport, 115200)
    
    def get_status(self):
        cmd = 'status\r\n'
        rc, rstr = self.send_status_cmd(cmd) 
        return(rc, rstr)

    def get_orientation(self):
        strin = "--"
        rc, rstr = self.get_status()
        if rc == 0:
            outstr = rstr.split('\n')
            cc1detect = None
            cc1led = None
            for instr in outstr:
                if 'CC1 detect:' in instr:
                    fstr = instr.split('0x')
                    cc1detect = int(fstr[1], 16)
                elif 'CC1 led:' in instr:
                    lstr = instr.split(':')
                    cc1led = int(lstr[1])
                    break
            if cc1led == 0 and cc1detect < 20:
                    strin = "Flip"
            elif cc1led == 1 and cc1detect > 20:
                strin = "Normal"
            return (rc, strin)
        else:
            return (rc, "ComError")