# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:32:37 2018

@author: Hp
"""

factorial = int(input('Enter your number.'))
x=1

if factorial > 0:
    for i in range(1,factorial+1):
        x = i*x
        print(x)
elif factorial == 0:
    print(1)
else:
    print('Does not exist for negative numbers.')