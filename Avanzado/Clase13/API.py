# pip3 install requests -- user (para poner utilizar el rquest, lo instalas en la terminal )

import requests
parametros = {
	"q":"perritos"
} 
"""
response = requests.get("https://randomuser.me/api/")
persona = response.json()

for i in persona:
	print(i, persona[i])

print(response.text)



for i in range(50):
	response = requests.get("https://randomuser.me/api/")
	persona = response.json()
	print(persona)

"""


#nos tiene que responder algo asi, el numero nos indica si hubo exito o no, y todos los 200 significan exito en la peticion     <Response [200]>

# requests.post()

response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyD6mmD4IzgNAgrUC6ewztxKX75Q9PAf2dA")
print(response.status_code)
print(response.json())