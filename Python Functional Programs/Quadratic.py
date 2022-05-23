# -*- coding: utf-8 -*-
"""
Created on Fri May 20 17:58:04 2022

@author: kavprabh
"""

import cmath

def Quadratic(a, b, c):
    delta = (b * b) - (4 * a * c)
    root1 = (-b + cmath.sqrt(delta)) / (2 * a)
    root2 = (-b + cmath.sqrt(delta)) / (2 * a)
    print(root1)
    print(root2)
    
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))

Quadratic(a, b, c)