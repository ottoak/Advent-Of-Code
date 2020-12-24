# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 16:53:11 2020

@author: Alex
"""

def num_paths0(A, min_path, cd, deleted=[]):
    
    paths = [A]
    
    if len(A)==len(min_path):
        return(paths)
    else:
        for x in cd:
            
            #print([x, cd, A])
            if can_delete(A, A.index(x)) and x not in deleted:
                deleted.append(x)
                new = [l for l in A if l!=x]
                
                paths.extend(num_paths0(new, min_path, [i for i in cd if i!=x], copy.deepcopy(deleted)))
                
            
        return(paths)
    
    # x1=['a','b','d','e']
# rev1 = list(chain.from_iterable(combinations(x1, i) for i in range(0,len(x1)+1)))

# x2=['a','c','d','e']
# rev2 = list(chain.from_iterable(combinations(x2, i) for i in range(0,len(x2)+1)))


# def num_paths(A,N_min, cd, deleted):
#     n=1
#     if len(A)==N_min:
#         return(1)
#     else:
#         for x in cd:
#             if can_delete(A, A.index(x)) and x not in deleted:
#                 deleted.append(x)
#                 n+=num_paths(A[0:A.index(x)]+A[A.index(x)+1:], N_min, [i for i in cd if i!=x], deleted[0:])
                
            
#         return(n)
    
def num_paths(A, N, cd, deleted=[]):
    
    paths = [A]
    
    if len(A)==N:
        return(paths)
    else:
        for x in cd:
            
            #print([x, cd, A])
            if can_delete(A, A.index(x)) and x not in deleted:
                deleted.append(x)
                new = [l for l in A if l!=x]
                
                paths.extend(num_paths(new, N, [i for i in cd if i!=x], copy.deepcopy(deleted)))
                
            
        return(paths)
    