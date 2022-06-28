import os
from minicps.states import SQLiteState
from sqlite3 import *

from utils import *


if __name__ == '__main__':
    try:
        SQLiteState._create(PATH, SCHEMA)
        SQLiteState._init(PATH, SCHEMA_INIT)
        print('{} succesfully created.'.format(PATH))
    except OperationalError:
        print('{} already exists.'.format(PATH))


    if os.path.isfile('room_temp.config'):
        print('room_temp.config already exists.')
    else:
        with open('room_temp.config', 'w+') as f:
            f.writelines([
                '## COMMENT TEMPERATURE WHEN USING RANDOM AND VICE VERSA ## \n',
                '\n\n',
                '# TEMPERATURE 26 <- EXAMPLE \n',
                '# TEMPERATURE 34 \n',
                '\n',
                '# RANDOM TEMPERATURE 12 42   <- EXAMPLE\n',
                'RANDOM TEMPERATURE 12 42'
                ])
        
        f.close()

        print('room_temp.config created.')
   