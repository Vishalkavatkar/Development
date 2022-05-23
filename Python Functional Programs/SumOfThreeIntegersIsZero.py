# -*- coding: utf-8 -*-
"""
Created on Sat May 21 09:23:37 2022

@author: kavprabh

@title : SumOfThreeIntegersIsZero
"""

def findTriplets(arr,m):
    flag = 0
    for i in range(0,m):
        for j in range(i+1,m):
            for k in range(j+1,m):
                if (arr[i]+arr[j]+arr[k]==0):
                    print(arr[i],arr[j],arr[k])
                    flag = 1
    if (flag == 0):
        print("Triplets not found")

arr=[]
n = int(input("Enter length of the array : "))
for i in range(n):
    arr.append(int(input("Enter a number : ")))
print(arr)
m = len((arr))
findTriplets(arr, m)