# -*- coding: utf-8 -*-
"""
Created on Tue May 10 18:00:23 2016

@author: cie1
"""

import heating.resistancevstemp as rt
import heating.polplots as pp
import matplotlib.pyplot as plt
import heating.conversions as conv
import heating.intensitycombo as com

rtfilepath='C:\\DOCUMENTS\\Projects\\Gratings\\Data\\2016\\May 4\\rvst.txt'
datafile1='C:\\DOCUMENTS\\Python Scripts\\1_9_1.txt'
datafile2='C:\\DOCUMENTS\\Python Scripts\\1_9_3.txt'
substratetemp=40.5
bias=0.03

t,r = rt.tempreader(rtfilepath)
drdt,b,equation = rt.rtlinearfit(t,r)
resistance,rerror = rt.findresistance(substratetemp,t,r)

a=pp.polplotreader(datafile1)
b=pp.polplotreader(datafile2)

intensity=conv.powertointensity(com.combinedata(a[0],b[0]))
dt=conv.xtodt(com.combinedata(a[1],b[1]),drdt,resistance,bias)




