# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from numpy import arange,array

ust = array([  1.41345315e-01,   7.68131167e-01,   1.46433093e-01,
         2.80893516e-26,   4.33366183e-22])

labels = ['RSSI Only', 'Phase Only', 'Cross', 'AND', 'OR']
plt.figure(figsize=(8,5))
for x,y in zip(arange(len(labels)),ust):
    plt.bar(x+1,ust[x],width=0.5,facecolor='lightgray',edgecolor='black')
    plt.text(x+1+0.25,y,'%s\n%.4f'%(labels[x],y),ha='center',va='bottom')
plt.xlim(0.5,6)
plt.ylim(0,1)
plt.xticks([])
plt.xlabel('Merge method')
plt.ylabel('P_value')
plt.title('Universal Statistical Test of different merge method')
plt.show()