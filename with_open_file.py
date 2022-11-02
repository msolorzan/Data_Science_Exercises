# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 20:28:52 2022

@author: MASN
"""

path = 'segismundo.txt'

f = open(path)

lines = [x.rstrip() for x in f]

f.close()

# =============================================================================
# Las siguientes líneas hacen lo mismo que las últimas tres
# =============================================================================
with open(path) as f:
    lines = [x.rstrip() for x in f]