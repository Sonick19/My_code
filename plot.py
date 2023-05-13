# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:57:44 2023

@author: соня
"""

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

import pandas as pd
d={'Overlaping':[], 'Similarity':[]}
with open('file for plot.txt') as inf:
    for line in inf:
        s =line.strip().split()
        s[0]=s[0].replace(",",".")
        s[1]=s[1].replace(",",".")
        s[1]=float(s[1])/100
        s[0]=round(float(s[0]),3)
        k=iter(s)
        for key in d:
            d[key].append(next(k))
adt=pd.DataFrame(d)
abt=adt[["Overlaping", "Similarity"]]
abt[["Similarity", "Overlaping"]].astype('float')    
print(abt)
plt.scatter(abt["Similarity"],abt["Overlaping"])
plt.ylim(0,0.7)
plt.xlim(0,1.1)
plt.ylabel('Overlaping')
plt.xlabel('Similarity')
plt.show()

    