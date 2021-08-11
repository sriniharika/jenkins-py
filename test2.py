# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:58:06 2021

Since callable instances are just normal instances , their classes can define any other method that u want
@author: NiharikaSrivastava
"""

import socket
class MyClass:
    def __init__(self): 
        self._cache={}
        
    def __call__(self,host):
        if host not in self._cache:
            self._cache[host]=socket.gethostbyname(host)
            
        return self._cache[host]
    
    def clear(self):
        self._cache.clear()
    
    def has_host(self,host):
        return host in self._cache
    
    