# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:20:43 2020

@author: Alex
"""
import fileinput
import numpy as np

d = []        
for line in fileinput.input('test.txt'):
      d.append(line.replace('\n',''))

L=np.array([[0,-1], [1,0]])
R=np.array([[0,1], [-1,0]])
Rot = {'L':L, 'R':R}

directions = {'N':np.array([0,1]), 'S':np.array([0,-1]), 'E':np.array([1,0]), 'W':np.array([-1,0])}

pos = np.array([0,0])
curr_dir = directions['E']
 
for a in d:
    if a[0]=='F':
        pos+=int(a[1:])*curr_dir
    elif a[0] in ['L', 'R']:
        curr_dir = np.linalg.matrix_power(Rot[a[0]],int(int(a[1:])/90)).dot(curr_dir)
    else:
        pos+=int(a[1:])*directions[a[0]]
                
print('Part 1: Manhattan distance is: {}\n'.format(abs(pos[0])+abs(pos[1])))

pos = np.array([0,0])
wp = np.array([10,1])

for a in d:
    if a[0]=='F':
        pos+=int(a[1:])*wp
    elif a[0] in ['L', 'R']:
        wp = np.linalg.matrix_power(Rot[a[0]],int(int(a[1:])/90)).dot(wp)
    else:
        wp+=int(a[1:])*directions[a[0]]
    
        print('Part 2: Manhattan distance is: {}'.format(abs(pos[0])+abs(pos[1])))       

    
