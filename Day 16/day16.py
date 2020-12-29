# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:03:38 2020

@author: Alex
"""

f = open("input.txt", "r")
ticket_info = f.readlines()
f.close()

nl_id = [i for i,x in enumerate(ticket_info) if x=='\n']
fields = [x.split(':')[0] for x in ticket_info[0:nl_id[0]]]
rules = [x.replace(' ','').replace('or','-').strip().split(':')[1] for x in ticket_info[0:nl_id[0]]]

nearby = [list(map(int, x.strip().split(','))) for x in ticket_info[nl_id[1]+2:]]

allowed = []
for i, r in enumerate(rules):
    r = list(map(int, r.split('-')))
    
    allowed.append(list(range(r[0], r[1]+1)))
    allowed.append(list(range(r[2], r[3]+1)))
    
allowed = set.union(*map(set, allowed))

remove_list=[]
c=0
for i, tckt in enumerate(nearby):
    for x in tckt:
        if x not in allowed:
            c+=x
            remove_list.append(i)

print(c)
nearby = [x for i, x in enumerate(nearby) if i not in remove_list]

fr = {x:[] for x in fields}

for i, r in enumerate(rules):
    r = list(map(int, r.split('-')))
    
    rules[i]=set(list(range(r[0], r[1]+1))+list(range(r[2], r[3]+1)))
    
for i in range(len(rules)):
    
    col = set([x[i] for x in nearby])
    
    for j, r in enumerate(rules):
        if col.issubset(r):
            
            fr[list(fr.keys())[j]]+=[i]
        

fr={k: v for k, v in sorted(fr.items(), key=lambda item: len(item[1]))}

for i,f in enumerate(fr.keys()):
    for j in range(i+1, len(fr)):
        fr[list(fr.keys())[j]].remove(fr[f][0])
        
print(fr)

mt = list(map(int, ticket_info[nl_id[0]+2:nl_id[1]][0].strip().split(',')))



    


     
