# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:45:44 2021

@author: NiharikaSrivastava
"""

DIGIT_MAP={
    'zero':0,
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9
    }

def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
    except KeyError:
        x = -1
        print(Exception(str))
        raise
    finally:
        print('inside finally')
        
    return x

print(convert("three fous".split()))

