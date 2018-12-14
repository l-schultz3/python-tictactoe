# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:41:10 2018

@author: l.schultz3
"""

import numpy as np

testArray = np.array([[None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0]])

for i in range(len(testArray)):
    if (testArray[i][0] == None and testArray[i][1] == 0):
        print(i)

testArray = np.append(testArray, [[10, 10]], axis=0)

print(testArray)