# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:48:48 2020

@author: Alex
"""
import fileinput
from copy import deepcopy
from itertools import product

class conway_grid_3d():
    
    def __init__(self, file):
        f = open(file, "r")
        I = f.readlines()
        
        init_state=[['.']*(len(I)+2)]
        for line in fileinput.input(file):
              init_state.append(['.']+list(line.strip())+['.'])
              
        init_state.append(['.']*(len(I)+2))      
        
        self.zdim=1
        self.N = len(init_state)
        
        self.state=self.build_grid(len(init_state), self.zdim)
        self.state[0]=init_state
        
        print('Running 3d model...')
        print('')
        for i in range(6):
            self.cycle()
            
        print('======== 3d Model =========')
        print('After 6 cycles:')
        self.count_active()
        print('===========================')
            
    def get_coords(self, x,y,z):
        coords = list(product( *[[x-1, x, x+1],[y-1, y, y+1], [z-1, z, z+1]] ))
        return [c for c in coords if c!=(x,y,z)]
            
    def count_active(self):
        c=0
        for z in range(-self.zdim, self.zdim+1):
            c+=([item for sublist in self.state[z] for item in sublist]).count('#')
        print('{} Active cubes'.format(c))

    def build_grid(self, n, z):
        return {i:[['.']*n for i in range(n)] for i in range(-z,z+1)}
        
    def cycle(self):
        new_grid = self.build_grid(self.N+2, self.zdim+1)
        for k in range(-self.zdim, self.zdim+1):
            for i in range(self.N):
                for j in range(self.N):
                    count=0
                    for I in self.get_coords(i,j,k):
                        try:
                            if self.state[I[2]][I[0]][I[1]]=='#':
                                count+=1
                        except IndexError:
                            continue
                        except KeyError:
                            continue
                        
                    if self.state[k][i][j]=='#' and count not in [2,3]:
                        new_grid[k][i+1][j+1]='.'
                    elif self.state[k][i][j]=='.' and count==3:
                        new_grid[k][i+1][j+1]='#'
                    else: 
                        new_grid[k][i+1][j+1]=self.state[k][i][j]
        
        self.state=new_grid
        self.N+=2
        self.zdim+=1
             
    def display(self,z):
        for x in self.state[z]:
            print(''.join(x))
        print('')
                        


