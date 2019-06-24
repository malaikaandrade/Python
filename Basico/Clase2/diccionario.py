#Diccionarios
x={}
x["red"]= "el color rojo"
x["green"]="el color verde"
print(x)

#Quiero imprimir en pantalla el color rojo
print(x["red"])
print(x["green"])

#llenando diccionario en una sola línea de código
y = {"red": "el color rojo", "green": "el color verde"}
print(y)

#Diccionario de varios tipos de datos
y = {"uno": 1, 2: "dos", 2.5:"numero flotante", "lista":[2,3,4,5,6,"hola"], (1,2,3): "una tupla"}

print(y[(1,2,3)])
print(y[2.5])
print(y["uno"])

#Alterando un valor
#reemplazamos [2,3,4,5,6,"hola"] con un "mundo"
y["lista"] = "mundo"
print(y)

#recuperando las llaves
claves = y.keys()
print(claves)
aux = list(claves)
print(aux)

#Recuperando valores
valores = y.values()
print(valores)
aux2 = list(valores)
print(aux2)

#Buscando valores
print("dos" in valores)

#Eliminar algo del diccionario
del y["uno"] #que me borre y en la llave uno
print(y)

del y
print (y)

