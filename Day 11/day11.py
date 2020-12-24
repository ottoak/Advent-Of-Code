# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:36:56 2020

@author: Alex
"""
import fileinput 
import numpy as np
import time
from copy import deepcopy

def ind_list(i,j):
        return [[i+1,j], [i-1,j], [i,j+1], [i,j-1], [i-1,j-1], [i-1,j+1], [i+1,j-1], [i+1,j+1]]
    
directions={'u':[-1,0], 'ur':[-1,1], 'r':[0,1], 'dr':[1,1], 'd': [1,0], 'dl':[1,-1], 'l':[0,-1], 'ul':[-1,-1]}

    
def adj_list(s, h, w):
        a=[ [ [] for i in range(w) ] for j in range(h) ]
    
        for i in range(h):
            for j in range(w):
                a[i][j]=[x for x in ind_list(i,j) if ((x[0]<h and x[0]>-1) and (x[1]<w and x[1]>-1))]
        return(a)

class seating_model:
    
    def __init__(self, in_file, p):
        
        t0=time.time()
        print('Initializing for part {}...'.format(p))

        self.seats= []
        
        for line in fileinput.input(in_file):
             self.seats.append(list(line.replace('\n','')))
        
        self.h=len(self.seats)
        self.w=len(self.seats[0])
        
        if p==1:
            self.adj = adj_list(self.seats, self.h, self.w)
        
        t1=time.time()
        print('Initialization done after {:.3f}ms.\n'.format((t1-t0)*1000))
        
        self.main_loop(p)

                        
    def count_filled(self, i, j, p):
        if p==1:
            return([self.seats[x[0]][x[1]] for x in self.adj[i][j]].count('#'))
        elif p==2:
            count=0
            for d in list(directions.keys()):
                i_n=i
                j_n=j
                
                while True:
                    i_n+=directions[d][0]
                    j_n+=directions[d][1]
                    
                    if (i_n<self.h and i_n>=0) and (j_n<self.w and j_n>=0):
                        if self.seats[i_n][j_n] in ['L', '#']:
                            if self.seats[i_n][j_n] =='#':
                                count+=1
                                
                            break
                    else:
                        break
            
            return(count)
                   
    def update(self, p):
        s_new=deepcopy(self.seats)
        
        for i in range(self.h):
            for j in range(self.w):
                if self.seats[i][j] == 'L' and self.count_filled(i,j,p)==0:
                        s_new[i][j]='#'
                elif self.seats[i][j] == '#' and self.count_filled(i,j,p)>=((p==1)*4+(p==2)*5):
                        s_new[i][j]='L'

        if (self.seats==s_new):  
            return True
        else:
            self.seats = s_new
            return False
                 
    def main_loop(self,p):
        print('Running simulation for part {}...'.format(p))
        t0=time.time()
        n=0
        done = self.update(p)
        while not done:
            n+=1
            # print('Still changing...')
            done = self.update(p)
        
        t1=time.time()
        print('\n===============================================')
        print('Stabilized after {} rounds and {:.3f}ms.'.format(n,(t1-t0)*1000))
        print('Number of occupied seats: {}.'.format([item for sublist in self.seats for item in sublist].count('#')))
        print('===============================================\n')
        
    def display(self):
        for x in self.seats: 
            print(''.join(x))
        print('\n')


sm = seating_model('input.txt',1)
sm = seating_model('input.txt',2)


    


