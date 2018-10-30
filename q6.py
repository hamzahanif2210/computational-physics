# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:22:14 2018

@author: Hp
"""

sentence = 'Sir, I m student'
reverse = sentence[::-1]
print('Reverse (letter by letter):' , reverse)


split_letter =  sentence.split(" ")
reverse_letter= split_letter[-1::-1] 
reverse_sentece = ' '.join(reverse_letter) 
print('Reverse (word by word):' , reverse_sentece )