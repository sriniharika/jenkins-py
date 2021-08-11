# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:49:46 2021

@author: NiharikaSrivastava
"""

g='global'

def outer (p='param'):
    l= 'local'
    def inner():
        print(g,p,l)
    inner()

outer()
    