#evaluar comparacuines

import random
x = random.randint(1,101)
"""
 if x<50:
 	print("El número es {0} y es menor a 50").format(x)

 else: 
 	print("El número es {0} y es mayor a 50").format(x)
"""

if x<10:
	print("El número es {0} y es menor a 10".format(x))

elif x>10 and x<20:
	print("El número es {0} y es mayor que 10 y menor que 20".format(x))

elif x>20 and x<30:
	print("El numero es {0} y es mayor que 20 y menor que 30".format(x))

else:
	print("El número es {0} y es mayor que 30".format(x))



