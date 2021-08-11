# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:30:05 2021

@author: NiharikaSrivastava

node js fs asynchronous operation

open()

open a file for reading or writing

file: path to the file (required)
"""

def myFunctionGenerator(n):
    for x in range(n):
        yield x*4

gen = myFunctionGenerator(4)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

