class miExcepcion(Exception):
	def __init__(self, mensaje):
		self.mensaje = mensaje

def unaFuncion(parametro = None):
	if parametro == None:
		raise miExcepcion("No puedes retirar dinero negativo del cajero.")


while True:
	print("Bienvenido a su banco MACAVI")
	print("Menú")

	print("¿Qué operación desea realizar?")
	print("1. Retirar dinero")
	print("2. Salir")

	eleccion = int(input("Opción: "))


	if eleccion == 1:
		cantidad = int(input("Ingresa el monto que deseas retirar: "))
		if cantidad == 0:
			unaFuncion()

		else:
			print("Cantidad retirada.")
			print("Hasta luego")


	elif eleccion == 2:
		print("Hasta luego")
		break


	