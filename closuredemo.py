# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:33:14 2021

@author: NiharikaSrivastava
"""

def sort_By_Last_Letter(strings):
    def Last_letter(s):
        return s[-1]
    print(Last_letter)
    return sorted(strings,key=Last_letter)

print(sort_By_Last_Letter(['hello','from','a','local','function']))


"""
python scoping rules

L- LOCAL
E- ENCLOSING
G- GLOBAL
B- BUILTIN
"""
def enclosing():
    x='closed over'
    def local_func():
        print(x)
    return local_func
    
lf=enclosing()
lf()

print(lf.__closure__)
