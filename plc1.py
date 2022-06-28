import random
import time
from minicps.devices import PLC

from utils import *

TEMP_SENSOR = ('TEMP_SENSOR', 1)


class HomePLC1(PLC):

    def pre_loop(self, sleep=0.1):
        print('DEBUG: plc1 in preloop')

        # temperature = 40
        # self.set(TEMP_SENSOR, temperature)
        time.sleep(sleep)

    def main_loop(self, sleep=0.4):
        print('DEBUG: plc1 in main loop')

        count = 0 
        while count < CYCLES:
            temperature = self.get_room_temperature()
            self.set(TEMP_SENSOR, temperature)

            # temperature = self.get(TEMP_SENSOR)
            self.send(TEMP_SENSOR, temperature, PLC1_ADDR)
            # print(temperature)

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
        protocol = PLC1_PROTOCOL,
        memory = PLC1_DATA,
        disk = PLC1_DATA
    )