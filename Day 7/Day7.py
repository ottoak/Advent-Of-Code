# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 13:30:58 2020

@author: Alex
"""
import re

data = open("input.txt", "r")
rules=[]
rules_v2=[]

for line in data:
    rules.append(line.replace('\n','')) 
    
    x=line.replace('\n','').split(" ")
    rules_v2.append([x[0]+' '+x[1], ' '.join([c for c in x[4:] ])])     
    
data.close()

allowed_colours = []
check_colours = ['shiny gold']

while len(check_colours)>0:
    new_colours = []
    for col in check_colours:
        for rule in rules:
            if col in ' '.join(x for x in rule.split(' ')[2:]):
                new_colours.append(rule.split(' ')[0]+' '+rule.split(' ')[1])
                
                
    allowed_colours.extend(new_colours)
    check_colours=new_colours

print(len(allowed_colours))
    
c_ind = {x.split(' ')[0]+' '+x.split(' ')[1]:i for i, x in enumerate(rules)}

def bags_in(col):
    cont = rules_v2[c_ind[col]][1]
    return([int(x) for x in re.findall('\d', cont)])
    
def bags_contained(col):
    cont = rules_v2[c_ind[col]][1].split(' ')
    if cont[0]=='no':
        return(0)
    else:
        return([cont[i]+' '+cont[i+1] for i in range(1,len(cont),4)])
        
def num_bags(col):
    if bags_contained(col)==0:
        return(0)
    else:
        n=0
        for i, c in enumerate(bags_contained(col)):
            n+= bags_in(col)[i]+bags_in(col)[i]*num_bags(c)

        return(n)

print(num_bags('shiny gold'))




    
    
    
    