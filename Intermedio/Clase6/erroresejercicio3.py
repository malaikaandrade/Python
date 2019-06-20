try:
	print(x) #tratamos de imprimir la variable "x" que no esta definida

except NameError:
	print("La variable x no esta definida")
#finally se ejecutara pase lo que pase
finally:
	print("Hasta pronto.")