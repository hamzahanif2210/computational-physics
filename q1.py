# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:00:41 2018

@author: Hp
"""
percentage = int(input('Please enter your percentage.'))

if percentage >= 80 :
    print('A+')
elif percentage >= 70:
    print('A')
elif percentage >= 60:
    print('B')
elif percentage >= 50:
    print('C')
elif percentage >= 40:
    print('D')
else:
    print('Fails')