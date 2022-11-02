# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:27:40 2022

@author: MASN
"""

with open('tmp.txt', 'w') as handle:
    handle.writelines(x for x in open('examples/segismundo.txt') if len(x) > 1)
    
with open('tmp.txt') as f:
    lines = f.readlines()