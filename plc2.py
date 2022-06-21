import time
from tkinter.tix import WINDOW
from minicps.devices import PLC

from utils import *

CURTAIN = ('CURTAIN', 2)
WINDOW = ('WINDOW', 2)
TEMP_SENSOR_1 = ('TEMP_SENSOR', 1)

class HomePLC1(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: plc2 in pre loop')
        time.sleep(sleep)

    def main_loop(self):
        print('DEBUG: plc2 in main loop')

        count = 0
        while True:
            curtain = self.get('CURTAIN')

            temperature = self.receive(TEMP_SENSOR_1, PLC1_ADDR)
            # print(temperature)

