import random
import time
from minicps.devices import PLC

from utils import *

TEMP_SENSOR = ('HR', 0, 'plc1')

class HomePLC1(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: plc1 in preloop')

        # temperature = 40
        # self.set(TEMP_SENSOR, temperature)
        time.sleep(sleep)

    def main_loop(self, sleep=0.5):
        print('DEBUG: plc1 in main loop')

        count = 0 
        while count < CYCLES or not CYCLES:
            temperature = self.get_room_temperature()
            self.set(TEMP_SENSOR, temperature)

            # print 'temperature: %d'%(temperature)
            # temperature = int(self.get(TEMP_SENSOR))
            
            print('temperature: {}'.format(temperature))
            self.send(TEMP_SENSOR, temperature, PLC1_ADDR+':'+PLC1_PORT)
            
            # val = self.receive(TEMP_SENSOR, PLC1_ADDR+':'+PLC1_PORT)
            # print 'revivied: %d'%(val)

            count += 1
            time.sleep(sleep)

    def get_room_temperature(self):
        with open('room_temp.config', 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            if line[0] == '#' or line[0] == '\n':
                continue
            else:
                s = line.split()

                if s[0] == 'TEMPERATURE':
                    return int(s[-1])
                elif s[0] == 'RANDOM':
                    return random.randint(int(s[-2]), int(s[-1]))

        f.close()


        

if __name__ == '__main__':

    plc1 = HomePLC1(
        name = 'plc1',
        state = STATE,
        protocol = PLC1_PROTOCOL
        # memory = PLC1_DATA,
        # disk = PLC1_DATA
    )