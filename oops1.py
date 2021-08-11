# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:33:38 2021

@author: NiharikaSrivastava
"""

class Flight:
    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError("no code'{number}'")
        if not number[:2].isupper():
            raise ValueError("invalid airline code '{number}'")
        if not number[:2].isdigit() and int(number[2:])<=9000:
            raise ValueError("invalid airline code in number '{number}'")
        self._number=number
        
        
    def number(self):
        return "sm123"
    def aircraft_model(self):
        return self._aircraft.model()
    
class Aircraft:
    def __init__(self,registration,model,num_rows,num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
        
    def registration(self):
        return self._registration
    
    def model(self):
        return self._model
    
    def seating_plan(self):
        return (range(1,self._num_rows+1),"ABCDEFGHIJK"[:self._num_seats_per_row])
"""
flight=Flight("sm123")
print(type(flight))
print(flight.number())
"""
"""
aircraft=Aircraft('A-8927','Airbus',num_rows=22,num_seats_per_row=0)
print(aircraft.seating_plan())
"""

flight=Flight('SM-1234',Aircraft('A-8927','Airbus',num_rows=22,num_seats_per_row=0))
print(flight.number())








