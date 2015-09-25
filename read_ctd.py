import os

#### CONFIG PARAMETERS ##########################
# pep-8 conventions suggest upper case for global variables
ROOTDIR = '/source/uerj_ocn_2015'
DATADIR = os.path.join(ROOTDIR, 'data')
FILENAME = os.path.join(DATADIR, 'ctd_bruto.cnv')

##### FUNCTIONS #################################

def parse_header(lines):
    for line in lines:
        if '**' in line:
            if 'S' in line or 'N' in line:
                try:
                    tmp = float(line.split()[1])
                    lat = line
                except ValueError:
                    pass

            if 'E' in line or 'W' in line:
                try:
                    tmp = float(line.split()[1])
                    lon = line
                except ValueError:
                    pass

    return lon[2:-2].strip(), lat[2:-2].strip()


def get_data():
    pass


#### BEGIN SCRIPT ###############################

f = open(FILENAME)
lines = f.readlines()

lon, lat = parse_header(lines)