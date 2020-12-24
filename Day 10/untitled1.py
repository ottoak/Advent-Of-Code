# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:02:43 2020

@author: Alex
"""

from collections import defaultdict

data = open("test.txt", "r")

adpt = [0]

for line in data:
    adpt.append(int(line))
data.close()

adpt.append(max(adpt)+3)
adpt.sort()

diffs = defaultdict(int)
counts = defaultdict(int, {0: 1})



for a, b in zip(adpt[1:], adpt):
    #print([a,b])
    diffs[a - b] += 1
    # number of ways to reach i'th adapter from previous three possible ones
    counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]
    print([a,counts[a]])

print(diffs[1] * diffs[3])
print(counts[adpt[-1]])