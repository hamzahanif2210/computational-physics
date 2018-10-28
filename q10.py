# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:40:33 2018

@author: Hp
"""

number = int(input('Of which number you want to see a multiplication table?'))
last = int(input('At which value you want to see the table?'))

for i in range (1,last+1):
    print(number,'x',i,'=',i*number)