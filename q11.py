# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:41:56 2018

@author: Hp
"""

Walk=input("Where do you take your next step? Forward, right, left or backward?")
steps = ['forward' , 'Forward' ,'FORWARD', 'right','Right','RIGHT' , 'Backward','backward','BACKWARD']

while Walk in steps:
  Walk=input("You are still lost. Take your next step.")
print("You are finally free.")
