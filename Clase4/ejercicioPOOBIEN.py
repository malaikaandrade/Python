class Alumno:
	#molde de los objetos
	def __init__(self, nombre, apellidos, matricula, materias, calificaciones):  #atributos

		self.nombre = nombre
		self.apellidos = apellidos
		self.matricula = matricula 
		self.materias = materias
		self.calificaciones = calificaciones
		self.promedio = sum(self.calificaciones)/5



while True:
	
	opcion = input("¿Desea agregar un Alumno")
	if opcion != "Salir":
		nombre = input("Ingrese el nombre: ")
		apellidos = input("Ingrese sus apellidos: ")
		matricula = input("Ingrese su matricula: ")
		materias = []
		calificaciones = []

		for materias in range(5):
			materia_actual = input("Ingrese la materia: ")
			calificacion_actual = input("Ingrese la calificacion: ")

		