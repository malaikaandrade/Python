listaDeNumeros = range (1,7+1)

print ("Números duplicados")

listaAuxiliar = []
for numero in listaDeNumeros:
	if numero != 4:
	
		listaAuxiliar.append(numero)
	listaAuxiliar.append(numero)

listaDeNumeros = listaAuxiliar
print (listaDeNumeros)
