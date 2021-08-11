# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:19:21 2021

@author: NiharikaSrivastava
"""

data = set([90,80,90,78])

print(type(data))

print(data)

for x in data:
    print(x)
    
data.add(80)
print(data)


clonedata=data.copy()

print(clonedata)

clonedata.update([1,2,3])

for x in data:
    print(x)
    
