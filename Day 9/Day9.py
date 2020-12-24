# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:13:42 2020

@author: Alex
"""

from itertools import combinations 
data = open("input.txt", "r")

code = []

for line in data:
    code.append(int(line))

data.close()

def code_break(cypher, N):
    #prv = cypher[0:N]
    ind = 0
    for i in range(N, len(cypher)):
        sums = list(map(sum , list(combinations(cypher[i-N: i], 2)) ))
        if cypher[i] not in sums:
            print('Found: first number is {}'.format(cypher[i]))
            ind = i
            break
    
    val = code[ind]
    test = code[0:ind]
    
    for l in range(0, len(test)):
        s = [test[l]]
        j = l+1
        while sum(s) < val:
            s.append(test[j])
            j+=1
            if sum(s) == val:
                print('== Encryption weakness found! ==')
                print('Sum of lowest numbers is: {}'.format(min(s)+max(s)))
                return([s, ind])
    
    return(ind)

x = code_break(code, 25)

    



