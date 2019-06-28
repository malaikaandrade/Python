import pygame
from time import sleep


#inicializamos pygame
pygame.init()

altoVentana = 228
anchoVentana = 510

#creamos una ventana
ventana = pygame.display.set_mode((anchoVentana, altoVentana))
pygame.display.set_caption("Mi primer juego con pygame")
reloj = pygame.time.Clock()

fondo = pygame.image.load('Sprites/desierto.png')

spritesDino = [pygame.image.load("Sprites/d1.png"), pygame.image.load("Sprites/d2.png"), pygame.image.load("Sprites/d3.png"), pygame.image.load("Sprites/d4.png")]

gameOver = pygame.image.load("Sprites/game_over.png")

#son las coordenadas para el objeto 

#declaramos características de dinosaurio: coordenadas(x,y), ancho, alto y velocidad
x = 0
y = 158
anchoDinosaurio = 40
altoDinosaurio = 60
velocidad = 5


#CACTUS
cactus = pygame.image.load("Sprites/cactus.png")
xCactus= 325
yCactus= 160
anchoCactus= 25
altoCactus= 48


# variable juego corriendo es verdadero mientras estamos jugando 
juegoCorriendo = True
#esta variable nos dice si esta saltando o no el dinosaurio 
estadoSaltando =False
contadorSalto = 10
contadorPasos = 0 #el contador es 0 porque empezraa a iterar nuestra lista desde la posicion 0 

ventana.blit(fondo,(0,0)) #Dibujamos el fondo de la ventana

#mientras sea verdadero juego corriendo haz esto
while juegoCorriendo:
	#pygame.time.delay(50)
	#es como si fuera un lisener, esta atento a la interaciión con el usuario.
	reloj.tick(12) # el 4 viene de los sprites que tenemos en nuestro dinosaurio

	for evento in pygame.event.get(): #recibimos uno por uno los eventos (iteracciones con usuario)
		if evento.type == pygame.QUIT: #si el evento es quit (presionar cerrar), se cierra la ventana y se acaba el juego
			juegoCorriendo=False

	teclas = pygame.key.get_pressed() #cuando una tecla se presiona se guardara en teclas


	if teclas[pygame.K_LEFT] and x>velocidad:
		x = x-velocidad
	#HACE REFERENCIA A LA TECLA DEL TECLADO DE LA COMPUTADORA PARA MOVERSE
	#cuando presiones esa tecla, haz una accion, 
	#cambiaremos de posicion por lo que cambiaremos su valor en x.
		
	if teclas[pygame.K_RIGHT] and x<(anchoVentana-anchoDinosaurio):
		x= x+velocidad
	if teclas[pygame.K_SPACE]:
		estadoSaltando=True
	if estadoSaltando == True:
		if contadorSalto >= -10:
			aux = 1
			if contadorSalto < 0:
				aux = -1
			y -= (contadorSalto**2) * aux*.35  #Los dos ** corresponden a elevar.
			contadorSalto -= 1

		else:
			estadoSaltando = False
			contadorSalto = 10
		contadorPasos += 1
	if contadorPasos >=4:
		contadorPasos = 0

	rectanguloDino = pygame.Rect(x,y, anchoDinosaurio, altoDinosaurio)
	rectanguloCactus = pygame.Rect(xCactus, yCactus, anchoCactus, altoCactus)

	if rectanguloDino.colliderect(rectanguloCactus):
		ventana.blit(gameOver,(50, 50))
		pygame.display.update()
		pygame.display.flip()
		sleep(2) # que se espere tantito antes de cerrarlo
		juegoCorriendo = False #si perdemos va a hacer que se cierre nuestra ventana




	ventana.blit(fondo,(0,0)) #Dibujamos el fondo de la ventana
	ventana.blit(spritesDino[contadorPasos],(x,y)) #la trupla (x,y) hace referencia a las coordenadas. #//division entre 4. el //le quita todos los decimales a la division
	ventana.blit(cactus, (xCactus,yCactus))
	#contadorPasos+=1



	pygame.display.update() #Para que se muestren lo que dibujamos debemos actualizar la pantalla

pygame.quit() #Cerramos pygame

"""
	
	pygame.draw.rect(ventana,(82,213,163),(x,y,anchoDinosaurio,altoDinosaurio)) #Dibujamos el dinosaurio (temporalmente un rectangulo)
	#(82,213,163) corresponde al color de nuestro rectangulo en código RGB


"""



