# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:25:42 2020

@author: Alex
"""
import math
import numpy as np

data = open("input.txt", "r")
codes=[]
for line in data:
    codes.append(line[:-1]) 
data.close()

def ul_half(code, r):
    if code == "u":
        return( [r[0]+math.ceil((r[1]-r[0])/2), r[1]] )
    elif code == "l":
        return( [r[0],  r[0]+math.floor((r[1]-r[0])/2)])
    
def decode(code):
    key = {"F":"l", "B":"u", "R":"u", "L":"l"}
    return "".join([key[c] for c in code])

seat_info=[]

for code in codes:
    r_row = [0,127]
    r_seat = [0,7]
    
    for c in decode(code[0:7]):
        r_row = ul_half(c, r_row)
        
    for c in decode(code[7:]):
        r_seat = ul_half(c, r_seat)
        
    seat_info.append([r_row[0],r_seat[0], r_row[0]*8+r_seat[0]])

ids = np.array(seat_info)[:,2]
print("The max seat id is {}".format(max(ids)))

for i in range(min(ids), max(ids)):
    if i not in ids:
        print("Your seat id is {}".format(i))
        break

    

    


    