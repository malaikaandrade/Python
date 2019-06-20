#Funciones en python
import math

def saludar():
	print("Hola a todo python am sala a (los mejores!)")

def suma(a,b):
	resultado = a+b 
	print("La suma es: ", resultado)
	return resultado
#todas las variables que declaremos e¡dentro de las funciones solo van a existir dentro de esa funcion. por lo que hay que ponerle el return. si. no lo pones va a dar un none (hay algo pero no se sabe que es)

def chicharronera(a,b,c):
	if a == 0:
		print("No se puede división entre cero :(")
	else:
		res1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
		res2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
		return res1, res2


saludar()
x = suma(3,8) # tenemos que guardar el resultado en alguna parte 
r1, r2 = chicharronera(1,2,1)

#print("Estoy fuera de la funcion y el resultado es: ",x)
print("La primer raíz es: ", r1)
print("La segunda raíz es ", r2)
