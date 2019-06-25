while True: 

	print("**************Bienvenido******************")
	print("*****************Menú*********************")

	print("Selecciona una opción: ")

	print("1. Calcular mi IMC")
	print("2. Salir")
	
	eleccion = int(input("opción: "))

	if eleccion == 1:
		print("Para calcular tu IMC necesitaremos que nos proporciones algunos datos.")

		x = int(input("Por favor ingresa tu peso: "))
		y = float(input("Por favor ingresa tu estatura: "))
		print("Tu IMC es de: ", x/(y*y))

	elif eleccion == 2:
		print("*************¡Hasta luego!****************")
		break

	else: 
		print("Digite otra opción: ")

