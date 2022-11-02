# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 22:03:22 2022

@author: MASN

"""

import numpy as np

arr = np.arange(1, 6)

float_arr = arr.astype('float64')

arr = np.array([1.3, 4.56, 6.7, 8.9, 45.0, -49.])

int16_arr = arr.astype('int16')

numeric_string = np.array(['1.2', '3.', '5.9'])

numeric_int = numeric_string.astype('float') # Se tiene que convertir a float, por los puntos decimales


