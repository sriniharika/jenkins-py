# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 14:48:09 2021

@author: NiharikaSrivastava


extended arguments syntax

abitary number of positional arguments
arbitary keyword arguments
"""

print("One","Two","Three",4,5,67,89)

print("{a}<====>{b}".format(a="IBM",b="INDIA"))
"""
def hyperVolume(*args):
    print(args)
    print(type(args))
  """
"""
def hyperVolume(val,*args): 
    i=iter(args)
    v=next(i)
    for args in i:
        v*=args
    return v

print(hyperVolume(8))
print(hyperVolume(89,97))
"""
"""" Rules for args must come after positional arguments
2. only collects positional arguments"""


def tag(name,**kwargs):
   result='<'+name
   for key, value in kwargs.items():
       result+=' {k}={v}'.format(k=key,v=str(value))
   result +='>'
   return result
    
print(tag('img',src='ibm.png',alt='ibmindia'))





