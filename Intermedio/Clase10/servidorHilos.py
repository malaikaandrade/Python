import threading
import socket
class HiloCliente(threading.Thread):
	def __init__(self, socketCliente):
		threading.Thread.__init__(self)
		self.socketCliente = socketCliente
#heredamos de threading la clase threading.Thread para heredar esa clase y poder crear un objeto de esa clase. 

#las acciones run son las que realiza(ejecuta) unicamente el cliente
	def run (self):
		while True:
			mensaje = self.socketCliente.recv(1024).decode()
			if mensaje == "adios":
				break
			print("mensaje: {0} desde: {1}".format(mensaje,str(threading.current_thread())))
		#nos regresa cual es el hilo que esta mandando el mensaje 
		self.socketCliente.close()
		#cerramos el socket
#es para ir guardando todos los clientes o todas las computadoras que se van a estar conectando

hilos = []

socketServidor = socket.socket() #de modulo socket creame un objeto de tipo socket
socketServidor.bind(("localhost", 3000))
print("Estamos esperando conexiones...")
socketServidor.listen(1)

while True:
	try:
		socketServidor.sttimeout(1) #marca cuando hay un tiempo de espera muy prolongado
		print("Esperando conexión....")
		socketCliente, direccion = socketServidor.accept() #guardamos el socket que se acaba de conectar y la direccion, lo acepra
		print("Conectado desde: ", direccion[0])
		# si se cansa de estar a la escucha
	except socket.timeout:
		print("Esperando...")
		continue


#cada cliente se comporta como un hilo con esto---- es por eso que en el init pasamos objeto de tipo socket
	hilo = HiloCliente(socketCliente)
	#a la lista hilo le estas agregando el objeto hilo, ----- append sirve para agregar elementos
	hilos.append(hilo)
	#iniciar la ejecucion de ese hilo
	hilo.start()
	#para saber que hilos estan conectados
	print(hilos)

socketServidor.close()


"""
socket: es una computadora (que esta conectada a un servidor) que recibe informacion y la manda a un servidor
se comportan como hilos porque realizan muchas funciones a la vez
"""