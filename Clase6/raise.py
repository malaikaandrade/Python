"""
raise

se usa para invocar errores

al invocar las excepciones se comportan como las excepciones que ya conociamoss

"""

while True:

	mejorCurso = input("Ingresa cual es el mejor curso de proteco: ")

	mejorCursoConMinusculas = mejorCurso.lower()

	if mejorCursoConMinusculas != "python am sala a":
		raise ValueError
	else: 
		print("Felicidades python AM es el mejor curso.")
		break


