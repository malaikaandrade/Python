Calculadora = True

while Calculadora:
	try:

		print("Calculadora")
		print("Menu")
		print("Selecciona una opción")

		print("1. Suma")
		print("2. Resta")
		print("3. Multiplicación")
		print("4.División")
		print("5. Salir")

		eleccion = int(input("opción: "))

		if eleccion == 1:
			num1 = int(input("Ingresa un número: "))
			num2 = int(input("Ingresa otro número: "))
			print("La suma de los dos números es: ", num1 + num2)

		elif eleccion == 2:
			num1 = int(input("Ingresa un número: "))
			num2 = int(input("Ingresa otro número: "))
			print("La Resta de los dos números es: ", num1 - num2)

		elif eleccion == 3:
			num1 = int(input("Ingresa un número: "))
			num2 = int(input("Ingresa otro número: "))
			print("La Multiplicación de los dos números es: ", num1 * num2)

		elif eleccion == 4:
			num1 = int(input("Ingresa un número: "))
			num2 = int(input("Ingresa otro número: "))
			print("La División de los dos números es: ", num1 / num2)

		elif eleccion == 5:
			print("Hasta luego")
			break

		else:
			print("Digite otra opción: ")

	except ZeroDivisionError:
		
		print("La division entre cero no es posible")
		seguir = input("¿Deseas realizar otra operación?")
		if seguir == "si":
			continue
		elif seguir == "no":
			break
		else:
			break

	else:
		print("Digite otra opción: ")