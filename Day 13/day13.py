# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 10:36:58 2020

@author: Alex
"""
import fileinput
import math

bus_info = []        
for line in fileinput.input('input.txt'):
      bus_info.append(line.strip())
      
T0 = int(bus_info[0])
ID=[int(x) for x in bus_info[1].split(',') if x!='x']
M=math.prod(ID)

a=[(int(x)-i)%int(x) for i, x in enumerate(bus_info[1].split(',')) if x!='x']
b = [int(M/x) for x in ID]
sol = [ai*bi*pow(bi,-1, mi) for ai, bi, mi in zip(a,b,ID)]

times = [x - T0%x for x in ID]
print("Part 1 solution: {}".format(ID[times.index(min(times))]*min(times)))     
print("Part 2 solution: {}".format(sum(sol)%M))

