import time
from minicps.devices import PLC

from utils import *

CURTAIN = ('CURTAIN', 2)
WINDOW = ('WINDOW', 2)
TEMP_SENSOR_2 = ('TEMP_SENSOR', 2)

class HomePLC1(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: plc2 in pre loop')
        time.sleep(sleep)

    def main_loop(self):
        print('DEBUG: plc2 in main loop')

        count = 0
        while count < CYCLES:
            curtain = self.get('CURTAIN')
            window = self.get('WINDOW')

            temperature = self.receive(TEMP_SENSOR_2, PLC1_ADDR)
            print(temperature)

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

