while True: #para que corra siempre que sea true
	cadena = input("Ingrese una cadena: ")
	if cadena == "salir":
		break #rompe nuestro ciclo 

	if cadena == "continuar":
		continue #hace que se salte lo que le prosiga dentro del ciclo ppero regresa y ejecuta el principio
	if cadena == "pasar":
		pass

	print("Tu cadena es: "+cadena)

