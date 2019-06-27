import pygame

pygame.init()

altoVentana = 228
anchoVentana = 510

ventana = pygame.display.set_mode((anchoVentana, altoVentana))

fondo = pygame.image.load('Sprites/desierto.png')
#son las coordenadas para el objeto 
x = 0
y = 158
anchoDinosaurio = 40
altoDinosaurio = 60
velocidad = 5


juegoCorriendo = True
juegoSaltando =False

while juegoCorriendo:
	pygame.time.delay(50)
	#es como si fuera un lisener, esta atento a la interaciión con el usuario.
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			juegoCorriendo=False



	teclas = pygame.key.get_pressed() #cuando una tecla se presiona se guardara en teclas


	if teclas[pygame.K_LEFT] and x>velocidad:
	#HACE REFERENCIA A LA TECLA DEL TECLADO DE LA COMPUTADORA PARA MOVERSE
	#cuando presiones esa tecla, haz una accion, 
	#cambiaremos de posicion por lo que cambiaremos su valor en x.
		x = x-velocidad

	if teclas[pygame.K_RIGHT] and x<(anchoVentana - anchoDinosaurio):
		x = x+velocidad

	if teclas[pygame.K_SPACE]:
		estadoSaltando = True

	ventana.blit(fondo,(0,0))
	pygame.draw.rect(ventana,(82,213,163),(x,y,anchoDinosaurio,altoDinosaurio))
	pygame.display.update()

pygame.quit()