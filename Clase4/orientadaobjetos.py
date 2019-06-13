class Persona:

	planeta = "Tierra"

	def __init__(self, nombre, apellido, edad):

		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad


	def saludar(self):

		print("Nombre: {nombre}".format(nombre=self.nombre))
		print("Apellido: {apellido}".format(apellido=self.apellido))
		print("Edad: {edad}".format(edad=self.edad))

	def saludar_a_otra_persona(self, otra_persona):
		
		print("Nombre: {nombre}".format(nombre=self.nombre))

#Instancia de persona
#Aqui se manda a llamar a inir y se le pasan los parametros que seran las caracteristicas de nuestro objeto

aldo = Persona("Aldo", "Vázquez", 21)
juan = Persona("Juan", "Andrade", 24)

#el objeto creado(juan, aldo) manda a llamar a su metodo saludar para realizar la accion
aldo.saludar()
juan.saludar()
print(aldo.planeta)
print(juan.planeta)


#los metodos dentro de una clase no pueden mandarse a llamar sin el objeto

