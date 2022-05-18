# -*- coding: utf-8 -*-
"""
Created on Wed May 18 00:09:55 2022

@author: kavprabh
"""

def prime_fact(x):
    prime_factors = []
    divisor = 2
    while divisor <= x:
        if x%divisor == 0:
            prime_factors.append(divisor)
            x = x/divisor
        else:
            divisor += 1
    return prime_factors

x = int(input("Enter Number to check all prime factors :"))
print(prime_fact(x))