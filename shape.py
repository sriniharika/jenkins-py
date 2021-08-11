# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:09:29 2021

@author: NiharikaSrivastava
"""

class Shape:
    def __init__(self,width,height):
        self._width=width
        self._height=height
    def calculateArea(self):
        raise NotImplementedError('Not implemented')
        
class Rectangle(Shape):
    def calculateArea(self):
        return self._width*self._height

class Triangle(Shape):
    def calculateArea(self):
        return .5*self._width*self._height
    
rectangle = Rectangle(23,89)
triangle= Triangle(20,90)
print(rectangle.calculateArea())
print(triangle.calculateArea())