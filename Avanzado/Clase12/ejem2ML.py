#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:26:17 2019

@author: cur01alu32
"""

from sklearn.datasets import load_iris

#creamos un objeto iris
iris = load_iris()

print(iris.feature_names)
print(iris.target_names)



print(iris.data[0])
print(iris.target[0])

"""
print(iris.target[0]) ---- nos devuelve la flor

0-- setosa
1-- versicolor
2-- virginica


print(iris.data[0])---- nos devuelve los datos de las medidas de su sepato y petalo
"""

for i in range (len(iris.target)):
    print("Dato {0}: label {1}, features {2}".format(i, iris.target[i], iris.data[i]))