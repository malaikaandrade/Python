#modelo red neuronal
#mi primer perceptron
"""
compuerta ADN

Entradas 		Salidas
0	0				0
0	1				0
1	0				0
1	1				1
"""
import random
import time

def funcion_activacion(x1,x2,w1,w2,b):
#aqui necesitamos poner dos entradas, dos pesos y un bias
	operacion = (x1*w1 + x2*w2) - b
	if operacion >= 0:
		return 1
	else:
		return 0

entradas = [(0,0),(0,1),(1,0),(1,1)]
salidas = [0,0,0,1]

w1 = 0.5
w2 = 0.2
b = 0.24
eta = 0.25


i = 0
for x in range(32):
	if i == 4:
		i = 0
		time.sleep(2)
		print()
# si i vale 4 reinicia su valor a 0, en las entradas

	x1 = entradas[i][0]
	x2 = entradas[i][1]
	D = salidas[i] #valores desado
	Y = funcion_activacion(x1,x2,w1,w2,b) 
	#valores obtenidos

	print(" x1 = {0} x2= {1} D= {2} Y= {3} w1= {4} w2= {5}".format(x1,x2,D,Y,w1,w2))

	#calculo del error

	delta = D - Y
	d1 = eta * delta * x1
	d2 = eta * delta * x2

	w1 += d1
	w2 += d2 

	b = b - eta * delta
	i+=1

