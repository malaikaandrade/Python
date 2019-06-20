import json

#json.dump() y json.load()

archivo_json = open("clase.json", "r")
diccionario = json.load(archivo_json)
print(diccionario)

diccionario["estatura"] = 1.70
habilidades = diccionario["habilidades"]
habilidades.append("bailar")
print(diccionario)
archivo_json.close()

archivo_json = open("clase.json", "w")
json.dump(diccionario, archivo_json, indent=4)






import csv

#sirve para escribir en un archivo
#row----linea escrita
row = ["Rodrigo", 21, "Vivas"]
archivo_csv = open("clase.csv", "w")

# csv.reader() y csv.writer()

salida= csv.writer(archivo_csv)
salida.writerow(row)

row = ["Malaika", 22, "Andrade"]
salida.writerow(row)

archivo_csv.close()
archivo_csv = open("clase.csv", "r")
lector = csv.reader(archivo_csv)

for fila in lector:
	print(fila)