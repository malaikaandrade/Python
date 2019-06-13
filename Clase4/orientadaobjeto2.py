class Persona:

	planeta = "Tierra"

	#molde de los objetos
	def __init__(self, nombre, apellido, edad):  #parametros 

		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.habilidades = []
		#no es necesario que venga como parametro pero entonces todos los objetos tendran una lista de habilidades
		#podemos alterar los valores de un objeto (como en el caso del metodo aprender que llenas la lista de cada objeto con las habilidades de cada uno)


	#metodos
	def saludar(self):

		print("{nombre} dice: Hola!".format(nombre=self.nombre))
		
	def saludar_a_otra_persona(self, otra_persona):
		
		print("{nombre} saluda a {otro}".format(nombre=self.nombre, otro=otra_persona.nombre))


	def aprender(self, nueva_habilidad):
		self.habilidades.append(nueva_habilidad)

	#decorador
	#es un metodo propio de la clase y no del objeto(osea es parte de la clase persona y todas las personas van a realizar este metodo(respirar))
	@classmethod
	def respirar(self):

		print("Todas las personas respiramos")



#Instancia de persona
#Aqui se manda a llamar a inir y se le pasan los parametros que seran las caracteristicas de nuestro objeto

#objetos
aldo = Persona("Aldo", "Vázquez", 21)
juan = Persona("Juan", "Andrade", 24)

"""
#el objeto creado(juan, aldo) manda a llamar a su metodo saludar para realizar la accion
aldo.saludar()
juan.saludar()
print(aldo.planeta)
print(juan.planeta)

#los metodos dentro de una clase no pueden mandarse a llamar sin el objeto

"""
"""
#aldo ejecuta la accion ç8toma el valor de self y rodrigo toma el valor de otra_persona
#self se refiere al valor que este al lado del punto.
aldo.saludar_a_otra_persona(juan)
juan.saludar_a_otra_persona(aldo)
"""

aldo.aprender("Dar clases")
juan.aprender("Bailar salsa")
aldo.aprender("Tocar un instrumento")
print("Habilidades de Aldo: {habs}".format(habs=aldo.habilidades))
print("Habilidades de Juan: {habs}".format(habs=juan.habilidades))
#podemos alterar las habilidades de un objeto

Persona.respirar()
