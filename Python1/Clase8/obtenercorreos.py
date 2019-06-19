import re

try:
	archivo = open("correos.txt", "r")
	contenido = archivo.read()
	print("Los correos electrónicos encontrados son: ")
	expresion = re.compile("[A-Za-z0-9\.-_]+@[A-Za-z0-9\.-_]+\.[A-Za-z0-9]+")
	# ESTO ("[\w\.-_]+[@\w\.-_]+\.[\w]") ES LO MISMO QUE ESTO ("[A-Za-z0-9\.-_]+@[A-Za-z0-9\.-_]+\.[A-Za-z0-9]+")
	# [\w\.-_]    cualquier caracter dentro de este conjunto puede o no puede ir 
	coincidencias =  expresion.findall(contenido)
	print(coincidencias)
	archivo.close()

except FileNotFoundError:
	print("No se encontró ningún archivo con ese nombre")
