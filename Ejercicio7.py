x={}
x["Nombre"]= ["Malaika", "Brenda", "Donaldo", "Aixa"]
x["Numero"]= ["5583986663", "5585674532", "5548905831", "5535056095"]

while True:

	print("Agenda personal")
	print("***********Menú**************")
	print("Selecciona una opción")

	print("1. Lista de contactos.")
	print("2. Añadir un contacto nuevo.")
	print("3. Eliminar un contacto.")
	print("4. Salir")

	opcion = int(input("\t=>"))

	if opcion == 1:
		print(x["Nombre"])
		print(x["Numero"])

	if opcion == 2:
		input("Ingresa el nombre del nuevo contacto",diccionario.update([Nombre]))

		
	elif opcion == 4:
		print("*************¡Hasta luego!****************")
		break

	else: 
		print("Digite otra opción: ")	
