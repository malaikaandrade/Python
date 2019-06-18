#Expresiones regulares

#secuencia especial de caracteres que ayuda a encontrar otras cadenas o conjuntos de cadenas utilizando una sintánxis mantenida en un patrón.

import re

#si la cadena coincide (hace match) regresa un objeto de tipo match, y si no, regresa none
#match verifica la coincidencia al inicio de la cadena si todas las primeras letras coincides va a decir que hizo match aunque al final de la cadena pongas otra letras, pero si al principio de la cadenas pones cualquier elemento que se diferente al original no lo va a contar como un match

if re.match("hola", " ko hola"):
	print("Hizo match 1")

if re.match("....", "tola"): #el . significa que puedes encontrar cualquier caracter seguido de la palabra ola
	print("Hizo match 2")

if re.match("\.ola", ".ola"):
	print("Hizo match 3")

if re.match("(pyy|l|o)ython", "lython"):
	print("Hizo match 4")

if re.match("niñ(o|a)s", "niñes"):
	print("Hizo match 5")

"""
[0-9]-obtiene un caracter del 0 al 9
[a-z]-caracter de la a la z
[A-Z]-caracter de la A a l Z
[0-9a-zA-Z]-Caracter dentro del rango de letras may y min y munericos

"""

if re.match("cadena[0-9]", "cadena1s"):
	print("Hizo match 6")

#negacion

if re.match("python[^0-9a-z]", "pythonA"):
	print("hizo match 7")

"""
cuantificadores

+,*,?,{}

+ -- el caracter que precede existe 1 o mas veces
* -- el caracter que precede existe 0 o mas veces
? -- el caracter que precede puede existir o no(1 o mas veces)
{n} -- n= numero de veces exactas que queremos que aparezca el caracter

"""

# la n debe existir por lo menos una vez
if re.match("python+", "pythonnnnnn"):
	print("Hizo match 8")

#la n puede o no existir
if re.match("python*", "pytho"):
	print("hizo match 9")

#con los parentesis le estamos indicando que busque esta combinacion de caracteres
if re.match("py(tho)?n", "pyn"):
	print("hizo match 10")

#las {} solo estan afectando a las letras h
if re.match("pyth{3}", "pythhhh"):
	print("hizo match 11")

"""
^ - debe ir al principio de la cadena
$ - Dede ir al final de la cadena

"""

if re.match("^(http|https)", "http://google.com"):
	print("hizo match 12")

if re.match("(.com)$", "google.com"):
	print("hizo match 13")



