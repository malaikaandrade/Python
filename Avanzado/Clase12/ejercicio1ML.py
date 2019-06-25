# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
machine learning

aprendisaje supervisando: caracteristicas asociadas a una etiqueta: 
    -arboles de decisión: estructura de datos para poder establecer un conjunto de reglas de decisión. El modulo para hacer arboles es el SKlearning
    -redes neuronales
aprendisaje no supervisado: caracteristicas, dependiendo de sus caracteristicas los puedes clasificar en diferentes grupos, y estas grupos tambien tienen cosas en comun
aprendisaje por refuerzo: por experiencia de la computadora, cuando hace algo mal recibe un castigo y cuando hace algo mal recibe un premio, por lo que va a tratar de solo hacer las cosas bien.


todos los datos que le damos a nuestra computadora para entrenarla se llama CONJUNTO DE ENTRENAMIENTO, 
LO IDEAL es que los datos con los que entrenamos a nuestra computadora no sean los miso con los que la vamos a probar, para ver si realmente aprendió, 
a este conjunto para ver si aprendió se le llama CONJUNTO DE PRUEBA.

#ARBOLES DE DECISION ---- SUPERVISADO
"""
from sklearn import tree

#Datos del clasificador

#caracteristicas (features)
"""
peso    textura     label
150     rugosa      naranja
170     rugosa      naranja
140     lisa        manzana
130     lisa        manzana

0 -- rugosa
1--- lisa
"""
features = [[150, 0], [170,0], [140, 1], [130,1]]
labels = ['naranja', 'naranja', 'manzana', 'manzana']

#CREAR NUESTRO ARBOL DE DECISION

clasificador = tree.DecisionTreeClassifier()
#de nuestro modulo arbol creame un objeto de tipo arbol de decision heredado del modulo tree, este objeto puede tener muchos metodos

#el algoritmo de aprendisaje incluido en el clasificador se llama 'fit'
clasificador = clasificador.fit(features, labels)

#REALIZAR PREDICCIONES 
print(clasificador.predict([[120, 0]]))

#para que nuestro algoritmo pueda funcionar correctamente se necesitan al menos 150 datos  
