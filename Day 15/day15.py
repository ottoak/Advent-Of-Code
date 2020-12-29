# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:04:07 2020

@author: Alex
"""
import time

n=30000000
inp = [0,13,1,8,6,15]

t0=time.time()

def mem_game(num, N):
    last_said={num: i + 1 for i, num in enumerate(num[:-1])}
    last_num = num[-1]
    
    for turn in range(len(inp)+1, N+1):
        last_turn=turn-1
        
        if last_num in last_said:
            new_num=last_turn-last_said[last_num]
        else:
            new_num=0
        
        last_said[last_num]=last_turn
        last_num=new_num
        
    return last_num

        
print('Said! Number said on turn {}: {}'.format(n, mem_game(inp, n)))     
     
t1=time.time()        
print('Time taken: {}s\n'.format(t1-t0))


