# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:59:37 2020

@author: Alex
"""
import numpy as np
import copy
import time
from collections import Counter
from itertools import chain, combinations


data = open("input.txt", "r")

adpt = [0]

for line in data:
    adpt.append(int(line))
data.close()

adpt.append(max(adpt)+3)
adpt.sort()

adpt=[0,1,2,3,6,7,10,11,12,13,14,17,18, 19, 22, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38]

def jolt_diffs(A):
    diff_counts = Counter(np.diff(A))
    print('# of 1 jolt diffs: {}, # of 3 volt diffs: {}'.format(diff_counts[1], diff_counts[3]))
    
    m_path=[0]
    
    while m_path[-1]!=max(A):
        if m_path[-1]+3 in A:
            m_path.append(m_path[-1]+3)
        elif m_path[-1]+2 in A:
            m_path.append(m_path[-1]+2)
        elif m_path[-1]+1 in A:
            m_path.append(m_path[-1]+1)
    
    
    return(m_path)

def can_delete(A, i):
    if A[i+1]-A[i-1]>3: 
        return(False)
    else:
        return(True)


cd_m = [x for i, x in enumerate(adpt[1:-1]) if can_delete(adpt, i+1)]
n=len(cd_m)
print(cd_m)

cd_trips=[[x, x+1, x+2] for x in cd_m if (((x+1) in cd_m) and ((x+2) in cd_m))]


# x=['a','b','c','d','e']
# rev = list(chain.from_iterable(combinations(cd_m, i) for i in range(0,len(cd_m)+1)))

def num_paths(A, min_path, cd, deleted=[]):
    
    paths = [A]
    
    if len(A)==len(min_path):
        return(paths)
    else:
        for x in cd:
            
            #print([x, cd, A])
            if can_delete(A, A.index(x)) and x not in deleted:
                deleted.append(x)
                new = [l for l in A if l!=x]
                
                paths.extend(num_paths(new, min_path, [i for i in cd if i!=x], copy.deepcopy(deleted)))
                
            
        return(paths)
    

d = jolt_diffs(adpt)

t1=time.time()

N1 = num_paths(adpt, d, cd_m, [])

t2=time.time()

print('Time elapse: {}s'.format(t2-t1))
print(len(N1))
  

    
