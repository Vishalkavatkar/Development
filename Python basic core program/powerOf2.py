# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:36:02 2022

@author: kavprabh
"""
power = int(input("Enter a number :"))
if power <= 31:
    for i in range(power):
        print(2**i)
else:
    print("Enter valid number")