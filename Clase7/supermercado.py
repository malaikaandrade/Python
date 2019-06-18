"""
Ejercicio

		Desarrollar un sistema para supermercado

		-El usuario agregará productos al carrito (nombre, cantidad)
		-El supermercado obtendrá los precios e imprimirá el ticket para el usuario

"""
import csv
archivo_csv = open("clase.csv", "w")

mercado = True

while mercado:


	print("**********Bienvenido al supermercado**********")
	print("Menú")
	print("Selecciona lo que deseas comprar")

	print("1. Manzana")
	print("2. Queso")
	print("3. Carne")
	print("4. Jamón")
	print("5. Leche")
	print("6. Salir")

	eleccion = int(input("opción: "))

	if eleccion == 1:
		Manzana = int(input("Ingresa la cantidad de manzanas que deseas comprar: "))
		total=Manzana*5
		print("El precio de la manzana es de $5 por unidad, tu total sería: ", total)

		row = ["El precio por unidad de la manzana es de: $5", "Tu total sería: {t}".format(t=total)]
		salida= csv.writer(archivo_csv)
		salida.writerow(row)

	elif eleccion == 2:
		Queso = int(input("Ingresa el número de Quesos que deseas comprar: "))
		total=queso*45
		print("El precio del Queso es de $45 por unidad, tu total sería: ", total)

		row = ["El precio por unidad del Queso es de: $45", "Tu total sería: {t}".format(t=total)]
		salida= csv.writer(archivo_csv)
		salida.writerow(row)

	elif eleccion == 3:
		Carne = int(input("Ingresa la cantidad de Carne que deseas comprar: "))
		total=Carne*128
		print("El precio de la Carne es de $128 por kilo, tu total sería: ", total)

		row = ["El precio de la Carne es de $128 por kilo", "Tu total sería: {t}".format(t=total)]
		salida= csv.writer(archivo_csv)
		salida.writerow(row)

	elif eleccion == 4:
		Jamon = int(input("Ingresa la cantidad de Jamón que deseas comprar: "))
		total=Jamon*89
		print("El precio del Jamón es de $89 por kilo, tu total sería: ", total)

		row = ["El precio del Jamón es de $89 por kilo,", "Tu total sería: {t}".format(t=total)]
		salida= csv.writer(archivo_csv)
		salida.writerow(row)

	elif eleccion == 5:
		leche = int(input("Ingresa la cantidad de Leche que deseas comprar: "))
		total=leche*18
		print("El precio de la leche es de $18 por unidad, tu total sería: ", total)

		row = ["El precio por unidad de la leche es de: $18", "Tu total sería: {t}".format(t=total)]
		salida= csv.writer(archivo_csv)
		salida.writerow(row)

	elif eleccion == 6:
		print("Hasta luego")
		archivo_csv.close()
		break

	else:
		print("Digite otra opción: ")


