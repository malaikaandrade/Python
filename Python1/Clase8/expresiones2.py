import re

if re.search("-\d{3}$", "099-333"):
	print("Hizo match")

if re.search("pytho.", "Este es el curso de python de la sala A"):
	print("Encontré una coincidencia")


#compile()me permite guardar mi expresión regular en una variable para despues usar otros metodos
patron = re.compile("a[3-5]+")

print(patron.match("a55"))

print(patron.findall("ba544 a222 a768 a3555 c55"))