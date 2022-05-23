# -*- coding: utf-8 -*-
"""
Created on Sat May 21 09:06:55 2022

@author: kavprabh

@Title : 2D Array
"""

def PrintArray(R, C):
    arr = []
    
    for i in range(R):
        abc = []
        for j in range(C):
            abc.append(input("Enter Element : "))
        arr.append(abc)
        
    for i in range(R):
        for j in range(C):
            print(arr[i][j], end = " ")
        print()
        
print("Enter number of rows : ")
R = int(input())

print("Enter number of columns : ")
C = int(input())

PrintArray(R, C)