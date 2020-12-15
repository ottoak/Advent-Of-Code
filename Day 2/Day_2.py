# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 16:35:53 2020

@author: Alex
"""
import re

data = open("AoC/Day 2/input.txt", "r")
pass_policies = data.read().split('\n')[:-1]
data.close()

x = pass_policies[2]

y = re.split('[-: ]',x)
count = 0

for line in pass_policies:
    x = re.split('[-: ]',line)
    if (x[-1].count(x[2])>=int(x[0])) and (x[-1].count(x[2])<=int(x[1])):
        count+=1

print(str(count)+'\n')
count=0

for line in pass_policies:
    x = re.split('[-: ]',line)
    i1 = int(x[0])-1
    i2 = int(x[1])-1
    pw = x[-1]
    ch = x[2]
   
    if bool(pw[i1]==ch) ^ bool(pw[i2]==ch):
        count+=1

print(count)

        