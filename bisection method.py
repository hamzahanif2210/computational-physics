# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:03:41 2018

@author: Hp
"""


import sympy as sym
import math

x = sym.Symbol('x')
f = sym.sympify(input("enter a formula: ")) #sy.sympify convert string object to symbol object

a=float(input("What is a?"))
b=float(input("What is b?"))
e= float(input("What is tolerance?"))
xold=0


while f.evalf(subs={x: a})*f.evalf(subs={x: b})>0:
    print("Choose new values of a and b")
    a=float(input("What is a?"))
    b=float(input("What is b?"))
    
while abs(f.evalf(subs={x: a}))>e and abs(f.evalf(subs={x: b}))>e:
    xmid=(a+b)/2
    error=(xmid-xold)
    print("a=",a,"f(a)=",f.evalf(subs={x: a}))
    print("b=",b,"f(b)=",f.evalf(subs={x: b}))
    print("x=",xmid,"f(x)=",f.evalf(subs={x: xmid}))
    print("Error=",error)
    print("")
    xold=xmid
    if f.evalf(subs={x: a})*f.evalf(subs={x: xmid}) < 0:
        b=xmid
    else:
        a=xmid


#600x4-550x3+200x2-20x-1