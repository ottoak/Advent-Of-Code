# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:06:53 2020

@author: Alex
"""

data = open("input.txt", "r")
import copy
import time

cmd = []
cmd_run = []

for line in data:
    l = line.replace('\n','')
    cmd.append([l[0],int(l[4:])]) 
    cmd_run.append(0)

data.close()

def run_program(cmd):
    acc = 0
    i=0
    c_run = cmd_run.copy()
    while i<len(cmd):
        if c_run[i]==1:
            print('Looped! Accumulator is {}'.format(acc))
            return(False)
            break
        else:
            if cmd[i][0]=='n':
                c_run[i]=1
                i+=1
            elif cmd[i][0]=='a':
                c_run[i]=1
                acc+=cmd[i][1]
                i+=1
            elif cmd[i][0]=='j':
                c_run[i]=1
                i+=cmd[i][1]
                
    print('Program complete, accumulator is {}'.format(acc))
    return True
            
run_program(cmd)

start=time.time()
for i in range(0,len(cmd)):
    cmd_2=copy.deepcopy(cmd)
    if cmd[i][0]=='n':
        cmd_2[i][0] = 'j'
        if run_program(cmd_2):
            break

        
    elif cmd[i][0]=='j':
        cmd_2[i][0]='n'
        if run_program(cmd_2):
            break


end=time.time()
print('\nTime elapsed: {}s'.format(end-start))




    
