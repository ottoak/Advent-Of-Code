# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:50:22 2020

@author: Alex
"""
import re
import pandas as pd

data = open("input.txt", "r")
passport=[]
l =""

for line in data:
    if line=='\n':
        passport.append(l)
        l=''
    else:
        l+=line
    
passport.append(l)
data.close()
  
keys = 'byr|iyr|eyr|hgt|hcl|ecl|pid|cid'
labels = sorted(keys[:-4].split('|'))

passport_v2 = []      

for x in passport:
    if (len(re.findall(keys, x))==8) or ((len(re.findall(keys, x))==7 and ('cid' not in re.findall(keys, x)))):
        passport_v2.append(sorted(x.replace('\n',' ').split()))
        
for x in passport_v2:
    for y in x:
        if y[0:3]!='cid':
            x[x.index(y)]=y[4:]
        else:
            x[x.index(y)]='cid'
    
    if 'cid' in x: x.remove('cid')
            
df = pd.DataFrame(passport_v2, columns = labels)
df = df[df['pid'].map(len) == 9]
df = df[df.hcl.str.contains("#")]
df = df[(df.hgt.str.contains("cm|in", regex=True))] 
df = df.astype({'byr':'int32', 'eyr':'int32', 'iyr':'int32'})
df = df[(df.byr < 2003) & (df.byr > 1919)]
df = df[(df.iyr < 2021) & (df.iyr > 2009)]
df = df[(df.eyr < 2031) & (df.eyr > 2019)]
df = df[(df.ecl.str.contains("amb|blu|brn|gry|grn|hzl|oth", regex=True))] 

df['hgt_m'] = df['hgt'].map(lambda x: x[-2:])
df['hgt'] = df['hgt'].map(lambda x: int(x[:-2]))

df = df[ ((df.hgt_m=='cm') & ((df.hgt<194) & (df.hgt>149))) | ((df.hgt_m=='in') & ((df.hgt<77) & (df.hgt>58))) ]
        
print(len(passport_v2))     
print(df.shape[0])  
