try:
	x=10/0

#inst sera nuestra variable
except ZeroDivisionError as inst:
	print(type(inst)) #imprime la instancia de la excepcion
	print(inst.args) #imprime los atgumentos guardados en .args
	print(inst) # __str__ permite imprimir directamente los argumentos

	