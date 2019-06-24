# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
lista = [1,2,4]
tupla =(1,2,3)
vector = np.array([2,3,4,5])
vector2 = np.array([6,7,8,9])

print(lista)
print(tupla)
print(vector)

#suma de vectores
suma = vector + vector2
print(suma)

#producto punto 
productoPunto = vector.dot(vector2)
print(productoPunto)

#creando matrices con el metodo array
m1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
m2 = np.array([[1],[3],[4]])
print(m1)
print(m2)

#multiplicacion de matrices usando array y metodo dot
print(m1.dot(m2))

#ARRAY CON UN RANGO DE VALORES
arr1 = np.arange(10)
print(arr1)
arr2 = np.arange(0,50,5)
print("\n", arr2)

#arreglos especiales
unos = np.ones((2,2)) #aqui no se pasan parametros, si el arreglo de los numeros para formar matrices o vectores
#el parametro pasa como tupla
print(unos)
#el punto que aparece se refiere a que es un flotante
ceros = np.zeros((3,5))
print(ceros)

#que vaya del 0 al 9 en 8 partes
lins = np.linspace(0,9,8)
print(lins)

#matriz diagonal
diagonal = np.eye(3)
print(diagonal)


#-----------------MATRIX-------------------
#transpuesta
matriz1 = np.matrix([[1,3,-5],[8, 9 , 10j]])
print(matriz1.T)

#hermitiana
print(matriz1.H)

#inversa
print(matriz1.I)

#MULTIPLICACION
m5 = np.matrix([[5,5,5,5],[6,6,6,6]]) #2x3
m6 = np.matrix([[4,4],[7,7],[8,8]]) #3x2

try:
    print(m5*m6)
    
except:
    print("Tu matriz no cumple con la regla, no se puede realizar.")



