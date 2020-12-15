# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:17:46 2020

@author: Alex
"""
import pandas as pd
from itertools import combinations
from functools import reduce
import operator


ER = pd.read_csv (r'AoC/Day 1/expense_report.csv', header=None, names=['Amt']).sort_values(by=['Amt'])['Amt'].tolist()

# Ugly
for i in range(0, len(ER)):
    
    for j in range(i+1, len(ER)):
        
        if (ER[i]+ER[j])==2020:
            print('{}, {}, {}'.format(ER[i], ER[j], ER[i]*ER[j]))
            break
      
for i in range(0, len(ER)):
    
    for j in range(i+1, len(ER)):
        
        if (ER[i]+ER[j])<2020:
            
            for k in range(i+1, len(ER)):
                
                if (ER[i]+ER[j]+ER[k])==2020:
                    
                    print('{}, {}, {}, {}'.format(ER[i], ER[j], ER[k], ER[i]*ER[j]*ER[k]))
                    break
          
print('\n')                
# Better
def P1(n):
    comb = combinations(ER,n)
    for c in comb:
        if sum(c)==2020:
            return reduce(operator.mul, c, 1)
        
print(P1(2))
print(P1(3))

#this is a test comment
print('x=4')


                
