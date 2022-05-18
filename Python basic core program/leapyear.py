# -*- coding: utf-8 -*-
"""
Created on Tue May 17 23:51:08 2022

@author: kavprabh
"""

def CheckLeap(Year):   
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
  else:  
    print ("Given Year is not a leap Year")  
Year = int(input("Enter the number: "))  
print(CheckLeap(Year))