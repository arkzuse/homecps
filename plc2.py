import time
# from typing import Protocol
from minicps.devices import PLC
from run import HomeCPS

from utils import *

CURTAIN = ('HR', 0, 'plc2')
WINDOW = ('HR', 1, 'plc2')
TEMP_SENSOR = ('HR', 0, 'plc1')

class HomePLC2(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: plc2 in pre loop')
        time.sleep(sleep)

    def main_loop(self, sleep=0.5):
        print('DEBUG: plc2 in main loop')

        count = 0
        while count < CYCLES or not CYCLES:
            temperature = self.receive(TEMP_SENSOR, PLC1_ADDR+':'+PLC1_PORT)
            # temperature = int(self.get(TEMP_SENSOR_2))

            if 16 <= temperature <= 28:
                window = 1
            else:
                window = 0
            
            if temperature >= 35:
                curtain = 0
            else:
                curtain = 1

            self.send(CURTAIN, curtain, PLC2_ADDR+':'+PLC2_PORT)
            self.send(WINDOW, window, PLC2_ADDR+':'+PLC2_PORT)

            self.set(CURTAIN, curtain)
            self.set(WINDOW, window)

            print('-----------')
            print('temperature {}'.format(temperature))
            print('curtain: {}'.format(curtain))
            print('window: {}'.format(window))

            count += 1
            time.sleep(sleep)

if __name__ == '__main__':

    plc1 = HomePLC2(
        name = 'plc2',
        state = STATE,
        protocol = PLC2_PROTOCOL
        # memory = PLC2_DATA,
        # disk = PLC2_DATA
    )