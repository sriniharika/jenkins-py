# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 13:16:47 2021

@author: NiharikaSrivastava
"""

orders1 = ['Iphone 12','Oneplus pro','Samsung Galaxy']

"""
print(sorted(orders1,key=lambda name:name.split()[-1]))

"""

last_name = lambda name: name.split()[-1]

print(last_name('Iphone 12'))