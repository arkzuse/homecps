# from minicps.utils import build_debug_logger

# home = build_debug_logger(
#     name=__name__,
#     bytes_per_file=10000,
#     rotating_files=2,
#     lformat='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     ldir='logs/',
#     suffix='')

CYCLES = 10

IP = {
    'plc1': '10.0.0.1',
    'plc2': '10.0.0.2',
    'plc3': '10.0.0.3'
}

MAC = {
    'plc1': '00.1A.2B.C7.BA.01',
    'plc2': '00.1A.2B.C7.BB.02',
    'plc3': '00.1A.2B.C7.BC.03'
}

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
PLC1_TAGS = (
    ('TEMP_SENSOR', 1, 'INT')
)
PLC1_SERVER = {
    'address': PLC1_ADDR,
    'tags': PLC1_TAGS
}
PLC1_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC1_SERVER
}

PLC2_ADDR = IP['plc2']
PLC2_TAGS = (
    ('CURTAIN', 2, 'INT'),
    ('WINDOW', 2, 'INT')
)
PLC2_SERVER = {
    'address': PLC2_ADDR,
    'tags': PLC2_TAGS
}
PLC2_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC2_SERVER
}

PLC3_ADDR = IP['plc3']
PLC3_TAGS = (
    ('AC_STATE', 3, 'INT'),
    ('AC_TEMP', 3, 'INT')
)
PLC3_SERVER = {
    'address': PLC3_ADDR,
    'tags': PLC3_TAGS
}
PLC3_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC3_SERVER
}


PATH = 'homecps_db.sqlite'
NAME = 'homecps_table'

STATE = {
    'name': NAME,
    'path': PATH
}

SCHEMA = """
    CREATE TABLE homecps_table (
        name    TEXT NOT NULL,
        pid     INTEGER NOT NULL,
        datatype    TEXT NOT NULL,
        value   TEXT,
        PRIMARY KEY (name, pid)
    );
"""

SCHEMA_INIT = """
    INSERT INTO homecps_table VALUES ('TEMP_SENSOR', 1, 'int', '25');
    INSERT INTO homecps_table VALUES ('CURTAIN', 2, 'int', '0');
    INSERT INTO homecps_table VALUES ('WINDOW', 2, 'int', '0');
    INSERT INTO homecps_table VALUES ('AC_STATE', 3, 'int', '0');
    INSERT INTO homecps_table VALUES ('AC_TEMP', 3, 'int', '25');
"""
