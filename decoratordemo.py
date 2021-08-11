# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:26:46 2021

@author: NiharikaSrivastava
"""

def escape_unicode(f):
    def wrap(*args,**kwargs):
        x=f(*args,**kwargs)
        return ascii(x)
    return wrap

@escape_unicode()
def my_Func():
    return '@$%%#$%#@mnk'


print(my_Func())