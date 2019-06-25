#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:36:08 2019

@author: cur01alu32
"""

from sklearn.datasets import load_iris
from sklearn import tree 
import numpy 


iris = load_iris()

#variable de prueba; obteniendo datos que se usaran como prueba
#setosa -- 0
prueba_target = iris.target[0]
prueba_data = iris.data[0]

"""
prueba_target = iris.target[50]
prueba_data = iris.data[50]

prueba_target = iris.target[100]
prueba_data = iris.data[100]
"""
#vamos a eliminar los numeros que vamos a usar como prueba, para poder probar bien nuestro programa
target = numpy.delete(iris.target,[0,50,100])
data = numpy.delete(iris.data,[0, 50, 100], axis=0)

clasificador = tree.DecisionTreeClassifier()


#aqui le estamos cargando todos los datos a nuestro programa, ose lo estamos entrenando
clasificador = clasificador.fit(data, target)

print("Datos de prueba")
print(prueba_target)
print(prueba_data)

print(clasificador.predict([prueba_data]))
print(clasificador.predict([[5, 3, 2, 2.5]]))