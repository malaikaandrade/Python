#Definicion de decorar

#se trata de una funcion que recibe como parametro otra funcion y devuelve una funcion 
#sirve para agregar mas acciones a nuestra funcion 
def agregar(funcion):
	def decorar():
		print("Esta a punto de iniciar mi funcion")
		funcion()
		print("Terminó la ejecucion")
	return decorar


#cuando mandas a llamar hola, tambien llamas a la funcion agregar ( esto para decorar)
#otra notaucion en lugar de agregar() es: agregar(hola)()

@agregar
def hola()
	print("hola")

hola()