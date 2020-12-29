# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 14:07:54 2020

@author: Alex
"""
import fileinput
import re
import numpy as np
from itertools import product
from collections import defaultdict


cmds = []        
for line in fileinput.input('input.txt'):
      cmds.append(line.strip().replace(' ','').split('='))
     
fileinput.close() 

mem = defaultdict(int)

def apply_mask(mask, val, p):
    if p==1:
        for i, x in enumerate(mask):
            if x!='X':
                val[i]=mask[i]
    elif p==2:
        for i, x in enumerate(mask):
            if x in ['X','1']:
                val[i]=mask[i]
                
    return val

                
def to_bin(x):
    val = '{0:b}'.format(int(x))
    val = list('0'*(36-len(val))+val)

    return val

# Part 1
for c in cmds:
    if c[0]=='mask':
        mask = c[1]
    else:
        val = apply_mask(mask, to_bin(c[1]),1)
        exec(c[0]+'='+str(int(''.join(val),2)))
        
print("Part 1 sum: {}".format(sum(mem.values())))

# Part 2

mem = defaultdict(int)

for c in cmds:
    if c[0]=='mask':
        mask = c[1]
    else:
        addr=np.array(apply_mask(mask, to_bin(int(''.join(re.findall('\d', c[0])))), 2))
        float_ids = [i for i,x in enumerate(addr) if x=='X']
        
        for x in product([0,1], repeat = len(float_ids)):
            addr[float_ids]=x
            mem[int(''.join(addr),2)]=int(c[1])
            
print("Part 2 sum: {}".format(sum(mem.values())))        


        