

while True:

	print("Calculadora")
	print("Menú")

	print("Selecciona una opción: ")

	print("1. Suma dos números")
	print("2. Elevar un número a la potencia n")
	print("3. Mostrar los números pares del 1 al 100")
	print("4. Salir")

	eleccion = int(input("opción: "))

	if eleccion == 1:
		num1 = int(input("Ingresa un número: "))
		num2 = int(input("Ingresa otro número: "))
		print("La suma de los dos números es: ", num1 + num2)

	elif eleccion == 2:
		num = int(input("Ingresa un número: "))
		pot = int(input("Ingresa la potencia a la que desees elevar el número: "))
		print("El número {0} elevado a la potencia {1} es: {2}".format(num, pot,num**pot))

	elif eleccion == 3:
		for x in range(1,100): 
			if x%2 == 0:
				print(x)

	elif eleccion == 4:
		print("Hasta luego")
		break

	else:
		print("Digite otra opción: ")

		