print("Suma de dos matrices.")

filas = int(input ("Introduzca el numero de filas de sus matrices: "))
columnas = int(input ("Introduzca el numero de columnas de sus matrices: "))

a = [[0 for i in range(columnas)] for j in range(filas)]
b = [[0 for i in range(columnas)] for j in range(filas)]
c = [[0 for i in range(columnas)] for j in range(filas)]


print ('Matriz 1: ')
for i in range(filas):
		for j in range(columnas):
			a[i][j] = int(input("Ingresar valor de la matriz 1: "))


print ('Matriz 2: ')
for i in range(filas):
		for j in range(columnas):
			b[i][j] = int(input("Ingresar valor de la matriz 2:"))




for i in range(filas):
	for j in range(columnas):
			c[i][j] = a[i][j] + b[i][j]

print("La suma de las matrices es: ")
for i in range (filas):
	for j in range (columnas):
		print (c[i][j])