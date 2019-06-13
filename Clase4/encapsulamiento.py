class Persona:

	planeta = "Tierra"

	#molde de los objetos
	def __init__(self, nombre, apellido, edad):  #atributos

		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.habilidades = []

		#los __ indican que este atributo es privado
		self.__telefono = "5555555555"

	def get_telefono(self):

		return self.__telefono

	def set_telefono(self, nuevo_numero):

		self.__telefono = nuevo_numero


aldo = Persona("Aldo", "Váquez", 21)

#no puedes acceder a un atriburo privado a menos que pongas get__
print(aldo.get_telefono())

#aldo.__telefono = "3333333" #ERROR no puedes modificar un objeto privado a menos que pongas set_

aldo.set_telefono("8787987987")
print(aldo.get_telefono())
