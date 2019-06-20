class Alumno:
	#molde de los objetos
	def __init__(self, nombre, apellidos, matricula, materias, calificaciones, promedio):  #atributos

		self.nombre = nombre
		self.apellidos = apellidos
		self.matricula = matricula 
		self.materias = materias
		self.calificaciones = calificaciones
		self.promedio = promedio

	def datos(self):

		print("Nombre: {nombre}".format(nombre=self.nombre))
		print("Apellido: {apellido}".format(apellido=self.apellido))
		print("Matricula: {matricula}".format(edad=self.matricula))

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
matricula = input("Ingresa tu matricula: ")
materias = input("Ingresa tus materias: ")
calificaciones = input("Ingresa tus calificaciones: ")

alu = Alumno()