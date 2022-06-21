import time
from minicps.devices import PLC

from utils import *

TEMP_SENSOR = ('TEMP_SENSOR', 1)


class HomePLC1(PLC):

    def pre_loop(self, sleep=0.1):
        print('DEBUG: plc1 in preloop')

        temperature = 37
        self.set(TEMP_SENSOR, temperature)

    def main_loop(self):
        print('DEBUG: plc1 in main loop')

        count = 0 
        while True:
            temperature = self.get(TEMP_SENSOR)
            self.send(TEMP_SENSOR, PLC1_ADDR)
            print(temperature)

            if count >= CYCLES:
                print('DEBUG: plc1 shutdown')
                break

            count += 1

        

if __name__ == '__main__':

    plc1 = HomePLC1(
        name = 'plc1',
        state = STATE,
        protocol = PLC1_PROTOCOL,
        memory = PLC1_DATA,
        disk = PLC1_DATA
    )