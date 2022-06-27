import time
from minicps.devices import PLC

from utils import *

AC_STATE = ('AC_STATE', 3)
AC_TEMP = ('AC_TEMP', 3)

TEMP_SENSOR_3 = ('TEMP_SENSOR', 1)


class HomePLC3(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: plc3 in pre loop')
        time.sleep(sleep)

    def main_loop(self):
        print('DEBUG: plc3 in main loop')

        count = 0
        while count < CYCLES:

            temperature = self.receive(TEMP_SENSOR_3, PLC1_ADDR)
            temperature = int(self.get(TEMP_SENSOR_3))

            if 16 <= temperature <= 28:
                ac_state = 0
            else:
                ac_state = 1 
            
            print('TEMPERATURE: {}'.format(temperature))
            
            if ac_state:
                if 28 <= temperature <= 35:
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


if __name__ == '__main__':

    plc1 = HomePLC3(
        name = 'plc3',
        state = STATE,
        protocol = PLC3_PROTOCOL,
        memory = PLC3_DATA,
        disk = PLC3_DATA
    )