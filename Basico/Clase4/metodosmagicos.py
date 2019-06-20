class Persona:

	planeta = "Tierra"

	#molde de los objetos
	def __init__(self, nombre, apellido, edad):  #parametros 

		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.habilidades = []

#Sobreescribe el metodo

	def __str__(self):

		return self.nombre+" "+self.apellido

	def __add__(self, otra_persona):

		return self.edad+otra_persona.edad

	def __len__(self):

		return len(self.habilidades)
		

aldo = Persona("Aldo", "Váquez", 21)
juan = Persona("Juan", "Andrade", 24)
print(aldo + juan)
print(len(aldo))