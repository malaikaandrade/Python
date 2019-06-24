#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:55:40 2019

@author: cur01alu48
"""

from sympy import *
#el * significa que quieres importar todas la biblioteca

#forzar tipo de dato
entero = 5 
transformacion = Float(entero)
print(transformacion)

fraccion = Rational(1,2)
fraccion2 = Rational(3,8)
entreCero = Rational(4,0)

suma = fraccion + fraccion2
print(suma)
print(entreCero)
