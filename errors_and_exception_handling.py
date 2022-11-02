# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:40:13 2022

@author: MASN
"""

def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError) :
        return x


x = attempt_float(input('Dame un valor: '))    
y = attempt_float((1, 2))    

print(x)

