# -*- coding: utf-8 -*-
"""
Created on Fri May 20 18:04:12 2022

@author: kavprabh
"""

import math

def Distance(x, y):
    distance = math.sqrt(pow(x, 2) + pow(y, 2))
    print(distance)
    
x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))

Distance(x, y)