# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:41:06 2020

@author: Alex
"""
import fileinput
from itertools import product

class conway_grid_4d():
    
    def __init__(self, file):
        f = open(file, "r")
        I = f.readlines()
        
        init_state=[['.']*(len(I)+2)]
        for line in fileinput.input(file):
              init_state.append(['.']+list(line.strip())+['.'])
              
        init_state.append(['.']*(len(I)+2))      
        
        self.zdim=1
        self.wdim=1
        self.N = len(init_state)
        
        self.state = self.build_grid(self.N, self.zdim, self.wdim)
        self.state[0][0] = init_state

        print('Running 4d model...')
        print('')
        for i in range(6):
            self.cycle()
            
        print('======== 4d Model =========')
        print('After 6 cycles:')
        self.count_active()
        print('===========================')
    
    def build_grid(self, n, z ,w):
        return {j:{i:[['.']*n for i in range(n)] for i in range(-z,z+1)} for j in range(-w,w+1)}
            
    def get_coords(self, x,y,z,w):
        coords = list(product( *[[x-1, x, x+1],[y-1, y, y+1], [z-1, z, z+1]], [w-1, w, w+1] ))
        return [c for c in coords if c!=(x,y,z,w)]
    
    def count_active(self):
        c=0
        for w in range(-self.wdim, self.wdim+1):
            for z in range(-self.zdim, self.zdim+1):
                c+=([item for sublist in self.state[w][z] for item in sublist]).count('#')
        print('{} Active cubes'.format(c))
            
    def cycle(self):
        new_grid = self.build_grid(self.N+2, self.zdim+1, self.wdim+1)
        for l in range(-self.wdim, self.wdim+1):
            for k in range(-self.zdim, self.zdim+1):
                for i in range(self.N):
                    for j in range(self.N):
                        count=0
                        for I in self.get_coords(i,j,k,l):
                            try:
                                if self.state[I[3]][I[2]][I[0]][I[1]]=='#':
                                    count+=1       
                            except IndexError:
                                continue
                            except KeyError:
                                continue
        
                        if self.state[l][k][i][j]=='#' and count not in [2,3]:
                            new_grid[l][k][i+1][j+1]='.'
                        elif self.state[l][k][i][j]=='.' and count==3:
                            new_grid[l][k][i+1][j+1]='#'
                        else: 
                            new_grid[l][k][i+1][j+1]=self.state[l][k][i][j]
        
        self.state=new_grid
        self.wdim+=1
        self.zdim+=1
        self.N+=2

    def display(self,z,w):
        for x in self.state[w][z]:
            print(''.join(x))
        print('')

                