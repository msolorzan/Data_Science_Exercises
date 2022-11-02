# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:48:34 2022

@author: MASN
"""


# =============================================================================
# LIST COMPREHENSION
# =============================================================================
# [expr for val in collectio if condition]
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']


[x.upper() for x in strings if len(x) > 2]

# =============================================================================
# DICT COMPREHENSION
# =============================================================================
# dict_comp = {key-expr: value-expr for value in collection if condition}
num = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}

# =============================================================================
# SET COMPREHENSION
# =============================================================================
# set_comp = {expr for value in collection if condition}

unique_lenghts = {len(x) for x in strings}
# Out[] {1, 2, 3, 4, 6}


set(map(len, strings))
# Out[] {1, 2, 3, 4, 6}

