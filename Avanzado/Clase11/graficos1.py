#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 10:48:57 2019

@author: malaikaandrade
"""

#matplotgit-- es una libreria para crear graficas

import matplotlib.pyplot as plt
import scipy as sp
import sympy as sm

#FIGURA 1
plt.figure(1)
ejeX = sp.linspace(1,10,100)
#del numero 1 hasta el 10 hazlo en 100 pedacitos
y = sp.cos(ejeX)
plt.xlabel('eje X')
plt.ylabel('Mi función coseno')
plt.title('Figura 1')
plt.plot(ejeX, y,  'm-.H')


#FIGURA2

plt.figure(2)
#esto hace que se creen dos nuevas graficas, si no lo ponen se grafica todo en una sola grafica
ejeX2 = sp.linspace(10, 50, 20)
g = sp.sin(ejeX2)
plt.xlabel('eje X')
plt.ylabel('Mi función seno')
plt.title('Figura 2')
plt.plot(ejeX2, g, 'c^--') 

#FIGURE 3
plt.figure(3)
with plt.style.context(('dark_background')):
    plt.plot(ejeX2, g, 'm^--')


plt.show()

