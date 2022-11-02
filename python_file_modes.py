# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:14:54 2022

@author: MASN
"""

f = open('examples/segismundo.txt')

f.read(12)

f2 = open('examples/segismundo.txt', 'rb')

f2.read(12)

f.tell()
f2.tell()

import sys

sys.getdefaultencoding()

f.seek(10)

f.read(1)


f.close()
f2.close()

