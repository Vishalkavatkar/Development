# -*- coding: utf-8 -*-
"""
Created on Fri May 20 17:42:44 2022

@author: kavprabh
@Title : WindChill Calculation
"""

def  WindChillCalculation(t,v):
    w=35.74+(0.6215*t)+((0.4275*t)-35.75)*pow(v, 0.16) #Formula
    print(w)
    
t = int(input("Enter the temperature in Farenheit is less than 50 : ")) 
v = int(input("Enter the wind speed in miles per/hour from 3 to 120 : "))

if v> 120 or v < 3 or t > 50:
    print("Enter Value in range")
else:
    WindChillCalculation(t,v)