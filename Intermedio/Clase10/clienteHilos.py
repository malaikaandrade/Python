import socket

socketCliente = socket.socket()

#direccion IP y puerto
socketCliente.connect(("192.168.3.13", 9000))

while True:
	mensaje = input("Ingresa tu mensaje: ")
	#se necesitan encodificar nuestros mensajes para que el servidor los pueda leer
	socketCliente.send(mensaje.encode()) #se hace con esta funcion
	if mensaje == "Adios":
		break


socketCliente.close()

"""
click---cola de procesos, cuando las computadoras se traban ocurre un error en un proceso

"""