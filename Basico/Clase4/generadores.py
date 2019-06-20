"""

Generadores
se definen igual que las funciones oero en la palabra retunr utiliza la palabra yield
generar datos de ejecucion

con yield puedes poner varios retornadores (CUANTOS YIELDS QUERAMOS) y ponerle que te devuelva diferentes valores 
"""

def generador():
	yield "hola"
	yield "adios"
	yield 1
	yield (3,3)

#puedo igualar una variable a una funcion, y ahora la variable se puede ejecutar como una funcion 
a = generador()

#los generadores regresan objetos iterables (los podemos visualizar mediaante un for)

#es un metodo magico que sirve para imprimir los yield uno por uno 
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

#Generador de números pares
#n me ayuda a saber cuantos numeros pares me faltan
#a me ayuda a saber si el numero es par o no
def pares(n): #n es el parametro de numeros pares que quiero obtener
	a = 0
	while n>0: #mientras que n sea mayor a 0 quiero que me ejecute diferentes funciones
		if a%2 == 0:
			yield a # si el numero que me generaste es divisible entre dos lo imprimo, y le resto uno al numero que me pediste (10-1)


			n = n-1 #asi le decimos: okey n ya te falta un numero menos

		a+=1 #si no es un numero par le incrementamos un uno (1+1=2 y ya es un numero par)

for num in pares(10):
	print(num)

