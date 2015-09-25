import os
import matplotlib.pyplot as plt

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


def get_data(lines):
    depth = []
    temp  = []

    for line in lines:
        if line[0] not in ['*', '#']:
            depth.append(float(line.split()[0]) * -1)
            temp.append(float(line.split()[1]))

    return depth, temp


def plot_data(temp, depth, lon, lat):
    plt.figure()
    plt.plot(temp, depth)
    title = "Temperature profile at location: %s, %s" %(lon, lat)
    plt.title(title)
    plt.xlabel('Temperature [C]')
    plt.ylabel('Depth [m]')
    plt.show()

#### BEGIN SCRIPT ###############################

f = open(FILENAME)
lines = f.readlines()

lon, lat = parse_header(lines)
depth, temp = get_data(lines)
plot_data(temp, depth, lon, lat)




