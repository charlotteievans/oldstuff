# -*- coding: utf-8 -*-
"""
Created on Sun May  8 00:06:45 2016

@author: cie1
"""

#determines whether or not it should plot a intensity plot or pol plot 
#does not save automatically

import os
from os import path

import heating.conversions as conv
import heating.polplots as pp
import heating.resistancevstemp as rt
import matplotlib.pyplot as plt

##change these values
rtfilepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\April 20\\rvst.txt'
polfilepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\April 20\\Iphoto redo\\1_10_10.txt'
figurepath='C:\\DOCUMENTS\\Projects\\Gratings\\Figures\\2016\\April 20\\'
os.makedirs(figurepath, exist_ok=True)
substratetemp=40.5
bias=0.05
plotlabel=path.splitext(path.basename(polfilepath))[0]
#leave this alone
t,r=rt.tempreader(rtfilepath)
drdt,b,equation=rt.rtlinearfit(t,r)
resistance,rerror=rt.findresistance(substratetemp,t,r)
power,x,pol=pp.polplotreader(polfilepath)
dt=conv.xtodt(x,drdt,resistance,bias)
pol_rad=conv.degtorad(pol)
intensity=conv.powertointensity(power)
pp.polpick(intensity, dt, pol_rad,plotlabel)
figbasename = plotlabel +'.png'
figfilepath = path.join(figurepath,figbasename)
plt.savefig(figfilepath,format='png')
