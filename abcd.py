import math

import heating.resistancevstemp as rt
from heating.Gphotomap_reader import gphoto_reader

gphotofilepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\Thermovoltage\\2_1_41.txt'
rtfilepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\Sept 21\\rvst.txt'
substratetemp=40.5
plotlabel='2-1 junction 300kOhm break'

def convert_current_to_voltage(current, resistance):
    return current*resistance

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

class MidpointNormalize(Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))

def thermovoltagemapplot(voltage,plotlabel,header):
    norm = MidpointNormalize(midpoint=0)
    im = plt.imshow(voltage.T, norm=norm, cmap=plt.cm.coolwarm,interpolation='none')
    plt.suptitle(plotlabel + '\nPolarization: ' + str(math.floor(header['Polarization'])) + ' degrees')
    plt.xlabel('x pixel')
    plt.ylabel('y pixel')
    clb = plt.colorbar(im, orientation='vertical')
    clb.set_label('Voltage (uV)', rotation=270, labelpad=20)
    plt.show()

header, arrays = gphoto_reader(gphotofilepath)
drdt, resistance = rt.get_drdt_and_resistance(rtfilepath, substratetemp)
current=arrays[0]
voltage=convert_current_to_voltage(current,resistance)
thermovoltagemapplot(voltage*1000000,plotlabel,header)