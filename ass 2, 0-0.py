# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:45:00 2018

@author: Hp
"""

import matplotlib.pyplot as plt 

h=[0,3,6,9,12,15,18,21,24,27,30,33]
D = [1.2,0.91,0.66,0.47,0.31,0.91,0.12,0.075,0.046,0.029,0.018,0.011]

plt.plot(h,D)
plt.xlim(0,33)
plt.xlabel(r'$h(km)$')
plt.ylabel(r'$D(kg/m^2)$')
plt.show()
plt.savefig("qua.png")
