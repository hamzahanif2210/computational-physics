# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:27:28 2018

@author: Hp
"""

factorial = int(input('Enter your number.'))
x=1
for i in range(1,factorial+1):
    x = i*x
    print(x)