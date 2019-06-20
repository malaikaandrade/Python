#Errores en python
"""
Error sintaxis
 try: 


Los errores detectadas durante la ejecucion se llamas excepciones, mhay dos formas de declarar un error: try and except

 Excepciones
except:

para que nos sirve manejar los errores en el codigo 
try y except van identados al mismo nivel 

el bloque try nos permite probar un pedazo de codigo que no sabes si contiene errores, una declaracion try puede tener mas de un except y nombrar multiples excepciones dentro de un ()

el bloque else se ejecutará solamente si el bloque try no causa ninguna excepcion,  ∫osea si no hay ningun error en nuestro codigo



"""

try:
	print(x)#tratamos de imprimir la variable x 
except NameError:
	print("La variable x no está definida")
except:
	print("Algo mas no está funcionando")


