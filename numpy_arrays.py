# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 22:02:07 2022

@author: MASN
"""

import numpy as np

data = np.random.randn(2, 3)

data_10 = data * 10

data_data = data + data

data1 = [6, 7.5, 8, 0, 1]

arr1 = np.array(data1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]

arr2 = np.array(data2)

arr1.dtype

arr2.dtype

np.zeros(10)

np.zeros([3, 6])

np.zeros([2, 3, 2])

empty = np.empty([2, 3, 2]) # No es confiable asumir que regresará solo ceros

np.arange(15)

np.full([2, 3], [1, 2, 3])

np.eye(3, 4)

