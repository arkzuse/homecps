import time
from typing import Protocol
from minicps.devices import PLC
from run import HomeCPS

from utils import *

CURTAIN = ('CURTAIN', 2)
WINDOW = ('WINDOW', 2)
TEMP_SENSOR_2 = ('TEMP_SENSOR', 1)

class HomePLC2(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: plc2 in pre loop')
        time.sleep(sleep)

    def main_loop(self):
        print('DEBUG: plc2 in main loop')

        count = 0
        while count < CYCLES:
            temperature = self.receive(TEMP_SENSOR_2, PLC1_ADDR)
            temperature = int(self.get(TEMP_SENSOR_2))

            if 16 <= temperature <= 28:
                window = 1
            else:
                window = 0
            
            if temperature >= 35:
                curtain = 0
            else:
                curtain = 1

            self.set(CURTAIN, curtain)
            self.set(WINDOW, window)

            count += 1

if __name__ == '__main__':

    plc1 = HomePLC2(
        name = 'plc2',
        state = STATE,
        protocol = PLC2_PROTOCOL,
        memory = PLC2_DATA,
        disk = PLC2_DATA
    )