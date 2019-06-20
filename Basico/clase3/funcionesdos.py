"""
#Asignar valores por defecto a los parámetros

def hola(a=5,b=6):
	print("La suma es: ",a+b)

#Tupla como argumento
def argumentos(*galileo):
	for x in galileo:
		print(x)
#el * significa un desempaque de la tupla de valores, los saca fuera de la tupla y los puedes ocupar 

#Diccionario como argumento
def diccionarios(**diccio):
	for x, y in diccio.items():
		print(x+" : "+y)

#dos * son porqu elos diccionarios tiene dos valores: llave y valor, necesita desempacar los dos
#items nos devuelve tanto llave como valor del diccionario


hola()
hola(2,3)
argumentos(6, "hola", 7, "mamamia", "python")
diccionarios(nombre="Aldo", edad=21, dinero="mucho", comer="verdura")
"""

#variables globales
numero = 20
print(numero)
def prueba():
	"""
	#variables locales-- solo existen dentro de una funcion
	numero = 15
	print(numero)
	"""
	#si queremos hacerla global 
	global numero
	numero = 30 
	print(numero)
prueba()
print(numero)
