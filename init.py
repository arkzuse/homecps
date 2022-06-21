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