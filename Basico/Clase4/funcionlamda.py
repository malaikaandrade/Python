#funcion normal

def f(x):
	resultado = x**2
	return resultado


#Lambda
g = lambda x: x**2
#las lambdas tambien se la pondemos asignarselas a una variable


print(f(3))
print(g(5))


#También podemos hacerlo de la siguiente manera
print((lambda x: x**4)(2))
# el dos es el valor de x

#Tarea opcional: 

#docs python.org