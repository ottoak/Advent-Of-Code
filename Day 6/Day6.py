# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:45:24 2020

@author: Alex
"""
data = open("input.txt", "r")
answers=[]
for line in data:
    if line =='\n':
        answers.append(line) 
    else:
        answers.append(line.replace('\n','')) 
data.close()

pos = [-1]+[index for index, c in enumerate(answers) if (c=='\n' or index==len(answers))]+[len(answers)]

group_ans=[answers[pos[i]+1:pos[i+1]] for i in range(0, len(pos)-1)]

counts=0
for ans in group_ans:
    counts+=len(set(''.join([x for x in ans])))
    
print('sum of counts is {}'.format(counts))

counts=0
for ans in group_ans:
    counts+=len(set.intersection(*[set(x) for x in ans]))
    
print('sum of second counts is {}'.format(counts))







    
