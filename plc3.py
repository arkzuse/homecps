from datetime import datetime
import logging
import time
from minicps.devices import PLC

from utils import *

AC_STATE = ('HR', 0, 'plc3')
AC_TEMP = ('HR', 1, 'plc3')

CURTAIN = ('HR', 0, 'plc2')
WINDOW = ('HR', 1, 'plc2')
TEMP_SENSOR = ('HR', 0, 'plc1')


class HomePLC3(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: plc3 in pre loop')
        time.sleep(sleep)

    def main_loop(self, sleep=0.5):
        print('DEBUG: plc3 in main loop')

        count = 0
        while count < CYCLES or not CYCLES:

            temperature = self.receive(TEMP_SENSOR, PLC1_ADDR+':'+PLC1_PORT)

            if 16 <= temperature <= 28:
                ac_state = 0
            else:
                ac_state = 1 
            
            print('-----------')
            print('temperature: {}'.format(temperature))
            
            if ac_state:
                if 28 <= temperature <= 35:
                    ac_temp = temperature - 10
                elif temperature > 35:
                    ac_temp = 16
                elif 5 <= temperature <= 15:
                    ac_temp = temperature + 10
                elif temperature < 15:
                    ac_temp = 30
                
                self.set(AC_TEMP, ac_temp)
                self.send(AC_TEMP, ac_temp, PLC3_ADDR+':'+PLC3_PORT)
                print('ac_temp: {}'.format(ac_temp))

            self.set(AC_STATE, ac_state)
            self.send(AC_STATE, ac_state, PLC3_ADDR+':'+PLC3_PORT)

            print('ac_state: {}'.format(ac_state))

            count += 1
            time.sleep(sleep)

            self.log_stats()


    def log_stats(self):
        t = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        with open('logs/stats.log', 'a+') as f:
            f.write('{}\t'.format(t))
            f.write('Room_temperature: {}  '.format(self.get(TEMP_SENSOR)))
            f.write('Curtain: {}  '.format(self.get(CURTAIN)))
            f.write('Window: {}  '.format(self.get(WINDOW)))
            f.write('AC state: {}  '.format(self.get(AC_STATE)))
            f.write('AC temperature: {}\n'.format(self.get(AC_TEMP)))
        f.close()



if __name__ == '__main__':

    plc3 = HomePLC3(
        name = 'plc3',
        state = STATE,
        protocol = PLC3_PROTOCOL
        # memory = PLC3_DATA,
        # disk = PLC3_DATA
    )