# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:12:06 2020

@author: Alex
"""

data = open("input.txt", "r")
hill=[]
for line in data:
    hill.append(line[:-1]) 
data.close()

def count_trees(slope, hill):
    s_x, s_y, w = slope[0], slope[1], len(hill[0])
    tree_count=0
    
    for i in range(s_y, len(hill), s_y):
        if hill[i][s_x*int(i/s_y)%w]=='#':
            tree_count+=1
               
    return(tree_count)


print(count_trees([1,1], hill))
print(count_trees([3,1], hill))
print(count_trees([5,1], hill))
print(count_trees([7,1], hill))
print(count_trees([1,2], hill))


        
    
    