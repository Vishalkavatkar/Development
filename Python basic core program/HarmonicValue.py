# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:08:44 2022

@author: kavprabh
"""

s = 0
n = int(input("Enter a number to check harmonic value :"))
if n != 0:
    for i in range (1, n+1):
        s = s + (1/i)
    print(s)
else:
    print("Enter valid number")
    

    
