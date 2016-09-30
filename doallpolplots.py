# -*- coding: utf-8 -*-
"""
Created on Sun May  8 00:27:41 2016

@author: cie1
"""

import heating.resistancevstemp as rt
import heating.polplots as pp
import os
from os import path
from heating.pathutil import listdir, onlytext
import matplotlib.pyplot as plt
import heating.conversions as conv

#change these
rtfilepath="C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\July 5\\r vs t.txt"
datapath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\July 5\\iPhoto'
figurepath="C:\\DOCUMENTS\\Projects\\Gratings\\Figures\\2016\\July 5\\iphoto"
substratetemp=40.5
bias=0.1

#leave the following alone
t,r = rt.tempreader(rtfilepath)
drdt,b,equation = rt.rtlinearfit(t,r)
resistance,rerror = rt.findresistance(substratetemp,t,r)
errors = []    
os.makedirs(figurepath, exist_ok=True)
#makes new folder for the figures
datafiles=onlytext(listdir(datapath))
for datafile in datafiles:
    try:
        power,x,pol = pp.polplotreader(datafile)
        dt = conv.xtodt(x,drdt,resistance,bias)
        pol_rad = conv.degtorad(pol)
        intensity = conv.powertointensity(power)
        plotlabel = path.splitext(path.basename(datafile))[0]
        figbasename = path.splitext(path.basename(datafile))[0]+'.png'
        figfilepath = path.join(figurepath,figbasename)
        pp.polpick(intensity, dt, pol_rad,plotlabel)
        plt.savefig(figfilepath,format='png')
        plt.close('all')
    except:
        errors.append(path.splitext(figbasename)[0])
        pass

    