# -*- coding: utf-8 -*-
"""
Created on Sat May 21 10:38:32 2022

@author: kavprabh

@Title - Gambler Program
"""

import random

stake = 100
goal = 200
win = 0
loose = 0
while (stake > 0 and stake < goal):
    toss = random.randint(0, 1)

    if toss == 0:
        stake -= 1
        loose += 1
    else:
        stake += 1
        win += 1

if stake >=200:
    print('"Gambler has won"')
else:
    print('"Gambaler has broke"')

print("Number of wins: ", +win)
print("Number of loose: ", +loose)
winPercentage = (win * 100) / (win + loose)
losspercentage = 100 - winPercentage
print("Win percentage is : ", winPercentage)
print("Loss percentage is : ", losspercentage)