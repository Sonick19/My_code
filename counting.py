# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:46:00 2022

@author: Sofiia
"""
s = []
d1 = {}
d2 = {}
counter = 0
sum1, sum2, sum3, counter = 0, 0, 0, 0
# open first file and create dictionary
with open('Y570 R2 TF.txt') as inf:
    for line in inf:
        s = line.strip().split()
        d1[s[0]] = [float(s[1]), float(s[2])]
#open seconf file and create dictionary
with open('Y570 R2 TN.txt') as inf:
    for line in inf:
        s = line.strip().split()
        d2[s[0]] = [float(s[1]), float(s[2])]
# set value of border in which coordinats can differ
border=4
#compare dictionaries   
for key in d1:
    for element in d2:
        if (d1[key][0]-d2[element][0]<=border) and(d1[key][0]-d2[element][0]>=-border) and (d1[key][1]-d2[element][1]<=border) and (d1[key][1]-d2[element][1]>=-border):
            counter += 1
            print(key, element)
print(counter)
