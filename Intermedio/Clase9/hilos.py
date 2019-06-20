#Hilos -- Threads

import threading

#hilos en python se implementan con la clase Thread

class Hilo(threading.Thread):

	def __init__(self, numero):
		threading.Thread.__init__(self)
		self.numero = numero

#dentro de este metodo van las acciones que queremos que hagan los hilos
	def run(self):
		for i in range(50):
			print(i)


#par imprimir una clase se necesita crear un objeto que va a ser hilo con su identificador 1

hilo = Hilo(1)
hilo2 = Hilo(2)

#para que los hilos empiecen su ciclo de vida necesitamos del metodo start() 
#el sistema operativo maneja el orden de los hilos y los tiempos de jecucion
#nosotros no podemos dar los tiempos de ejecucion

hilo.start()
hilo2.start()

