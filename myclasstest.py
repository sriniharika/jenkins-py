# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:12:12 2021

@author: NiharikaSrivastava
"""

def myFunc():
    print('hello')
    
from test2 import MyClass

print(MyClass)
print(myFunc)


instance = MyClass()


"""
print(instance('ibm.com'))

print(instance.__call__('google.com'))

print(instance._cache)

print(instance('ibm.com'))
print(instance.has_host('ibm.com'))

instance.clear()
print(instance.has_host('ibm.com'))
"""