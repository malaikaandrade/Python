import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = "localhost"   #tambien se pueden usar "127.0.0.1"
ip_addres = "192.168.3.48"

print("Servidor {0} ip: {1}".format(hostname, ip_addres))

complete_address = (ip_addres, 3000) #el segundo parametro representa al puerto al que queremos ingresar
#las ip completas llevan la forma xxx.xxx.xxx.xxx:puerto
sock.bind(complete_address)

sock.listen(1)
#va a preparar el puerto para que espere conexiones

while True:
#este detecta las conexiones

	print("Esperando cliente...")
	conexion, direccion_cliente = sock.accept() #acepta las conexiones

# el segundo while conecta con servidor 
	try:
		while True: 
			print("Cliente desde: {0}".format(direccion_cliente))
			data = conexion.recv(64) 
			#el 64 es el tamaño de los bytes 
			if data:
				print(data.decode())
				#contesta el cliente un cadena y esta la convertimos a bytes para que la computadora la pueda entender
				#cuando estamos mandado informacion al cliente esto lo generamos en forma de cadena asi con la funcion encode lo transforma en bytes para que la computadora lo pueda entender
				respuesta = input(">> ")
				respuesta_bytes = respuesta.encode("utf-8")
				conexion.sendall(respuesta_bytes)
			#para que sepa que decodificacion estamos usando; puede ser utf-8 o ASCII
			#decodificamos lo sbytes para leerlos como una cadena
			

	except Exception as e:
		print (e)
		print("no hay clientes disponibles")
		break
	finally:
		conexion.close() 
