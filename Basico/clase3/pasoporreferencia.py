#paso por valor
#unicamente se manda una copia de mi variable principal a la funcion 
"""
esto ocurre solo con tipos de datos simples
enteros, flotantes
"""
#paso por valor 

n = 10
def duplicar(parametro):
	parametro = parametro*2
	print(parametro)

print(n)
duplicar(n)
print(n) #se imprime el mismo valor que le diste al principio-- paso por valor

lista = [2,3,4]

#paso por referencia

def duplica(l):
	for x in range(len(lista)):
		l[x] = l[x]*2
		#print(l[x])
	print(l)

print("Lista",lista)
#print("duplica",duplica(lista))
duplica(lista[:])#asi solo imprime la copia de la primer lista, sin su modificacion
duplica(lista.copy())#asi solo imprime la copia de la primer lista, sin su modificacion

print(lista) #se imprime el ultimo valor que adquirió la lista