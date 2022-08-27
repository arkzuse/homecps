from minicps.utils import build_debug_logger

home = build_debug_logger(
    name=__name__,
    bytes_per_file=10000,
    rotating_files=2,
    lformat='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    ldir='logs/',
    suffix='')

#set CYCLES = 0 for infinite loop
CYCLES = 0
# CYCLES = 100000

IP = {
    'plc1': '10.0.0.1',
    'plc2': '10.0.0.2',
    'plc3': '10.0.0.3',
    'attacker': '10.0.0.4',
}

MAC = {
    'plc1': '00.1A.2B.C7.BA.01',
    'plc2': '00.1A.2B.C7.BB.02',
    'plc3': '00.1A.2B.C7.BC.03',
    'attacker': '00.1A.2B.C7.BD.04',
}

#modbus server port
PLC1_PORT = '502'
PLC2_PORT = '502'
PLC3_PORT = '502'
ATTACKER_PORT = '502'

PLC1_DATA = {
    'TEMP_SENSOR': '25'
}
PLC2_DATA = {
    'CURTAIN': '0',
    'WINDOW': '0',
}
PLC3_DATA = {
    'AC_STATE': '0',
    'AC_TEMP': '25',
}


PLC1_ADDR = IP['plc1']
PLC1_TAGS = (10, 10, 10, 10)

PLC1_SERVER = {
    'address': PLC1_ADDR,
    'tags': PLC1_TAGS
}
PLC1_PROTOCOL = {
    'name': 'modbus',
    'mode': 1,
    'server': PLC1_SERVER
}

PLC2_ADDR = IP['plc2']
PLC2_TAGS = (10, 10, 10, 10)
PLC2_SERVER = {
    'address': PLC2_ADDR,
    'tags': PLC2_TAGS
}
PLC2_PROTOCOL = {
    'name': 'modbus',
    'mode': 1,
    'server': PLC2_SERVER
}

PLC3_ADDR = IP['plc3']
PLC3_TAGS = (10, 10, 10, 10)
PLC3_SERVER = {
    'address': PLC3_ADDR,
    'tags': PLC3_TAGS
}
PLC3_PROTOCOL = {
    'name': 'modbus',
    'mode': 1,
    'server': PLC3_SERVER
}

ATTACKER_ADDR = IP['attacker']


NAME = 'homecps_db'
PATH = 'homecps_db.sqlite'

STATE = {
    'name': NAME,
    'path': PATH
}


'''
('HR', 0, 'plc1', '25') : TEMPERATURE_SENSOR
('HR', 0, 'plc2', '0')  : CURTAIN 
('HR', 1, 'plc2', '0')  : WINDOW
('HR', 0, 'plc3', '0')  : AC_STATE
('HR', 1, 'plc3', '25') : AC_TEMPERATURE
'''

SCHEMA = """ 
CREATE TABLE homecps_db (
    type              TEXT NOT NULL,
    offset            INT  NOT NULL,
    pid               TEXT  NOT NULL,
    value             TEXT,
    PRIMARY KEY (type, offset, pid)
);
"""

SCHEMA_INIT = """
    INSERT INTO homecps_db VALUES ('HR', 0, 'plc1', '25');
    INSERT INTO homecps_db VALUES ('HR', 0, 'plc2', '0');
    INSERT INTO homecps_db VALUES ('HR', 1, 'plc2', '0');
    INSERT INTO homecps_db VALUES ('HR', 0, 'plc3', '0');
    INSERT INTO homecps_db VALUES ('HR', 1, 'plc3', '25');
"""
