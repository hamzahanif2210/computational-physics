# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:05:24 2018

@author: Hp
"""


eng_sub= int(input('Enter the marks of your english paper.'))
urdu_sub= int(input('Enter the marks of your urdu paper.'))
math_sub= int(input('Enter the marks of your math paper.'))
phy_sub= int(input('Enter the marks of your physics paper.'))
chem_sub= int(input('Enter the marks of your chemistry paper.'))

total = eng_sub+urdu_sub+math_sub+phy_sub+chem_sub
percentage = (total/500)*100

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