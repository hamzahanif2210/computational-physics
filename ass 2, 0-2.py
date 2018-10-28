# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:45:10 2018

@author: Hp
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1,100,2)
y= x**4*np.e**-2*x
z= x*np.sin(x)+np.cos(x)


plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title('Two graphs in one ')
plt.ylabel(r'$x^4e^{-2x}$')
    

plt.subplot(2, 1, 2)
plt.plot(x, z)
plt.xlabel(r'$Range$')
plt.ylabel(r'$x\,cosx+sinx$')
plt.show()