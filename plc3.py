import time
from minicps.devices import PLC

from utils import *

AC_STATE = ('AC_STATE', 3)
AC_TEMP = ('AC_TEMP', 3)

SENSOR_TEMP_3 = ('SENSOR_TEMP', 3)


class HomePLC3(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: plc3 in pre loop')
        time.sleep(sleep)

    def main_loop(self):
        print('DEBUG: plc3 in main loop')

        count = 0
        while count < CYCLES:

            ac_state = self.get(AC_STATE)
            ac_temp = self.get(AC_TEMP)

            temperature = self.receive(SENSOR_TEMP_3, PLC1_ADDR)

            if 16 <= temperature >= 28:
                ac_state = 1
            else:
                ac_state = 0 
            
            if ac_state:
                if 28 <= temperature >= 35:
                    ac_temp = temperature - 10;
                elif temperature > 35:
                    ac_temp = 16
                elif 5 <= temperature <= 15:
                    ac_temp = temperature + 10
                elif temperature < 15:
                    ac_temp = 30

            self.set(AC_STATE, ac_state)
            self.set(AC_TEMP, ac_temp)

            count += 1