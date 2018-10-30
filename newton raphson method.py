# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 19:38:14 2018

@author: Hp
"""

import sympy as sym
import math

x = sym.Symbol('x')
f = sym.sympify(input("enter a formula: ")) #sy.sympify convert string object to symbol object
fd = f.diff(x)
    


 

a=float(input("What is a?"))
tol=abs(float(input("What is tolerance?")))
error=1

while fd.evalf(subs={x: a})==0:
    print("Choose a different initial value.")
    a=float(input("What is a?"))
while error>tol:
    p=a-(f.evalf(subs={x: a})/fd.evalf(subs={x: a}))
    error=abs((p-a)/p)
    print("a=",a,"f(a)=",f.evalf(subs={x: a}))
    print("p=",p,"f(p)=",f.evalf(subs={x: p}))
    print("Error=",error)
    print("")
    a=p
if error<tol:
    print("The root of the given equation ,", f,'is,' ,a)


#600x4-550x3+200x2-20x-1