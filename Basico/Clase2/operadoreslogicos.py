#comparaciones multiples con operadores logicos

"""
0R: "O" y si alguna de las dos o mas condiciones es TRUE y se ejecuta el codigo
NOT: "no" y si la primera condicion se cumple y la segunda no se ejecuta el codigo
"""

x = int(input("Ingrese un número: "))

if x%2!=0:
	print("El número {0} es impar".format(x))

if x%3==0 or x%5==0: 
	print("El numero es divisible entre 3 y entre 5".format(x))

#el not solo acepta un parametro
if not x%5==0:
	print("El numero {0} es divisible entre 3 pero no entre 5".format(x))

if x%3==0 and not x%5==0:
	print("El numero {0} es divisible entre 3 pero no entre 5".format(x))


#el {0} sirve para que dentro de este espacio puedas poner el numero