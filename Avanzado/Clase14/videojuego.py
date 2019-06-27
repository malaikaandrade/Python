"""
display-- el display es lo que tu ves en la pantalla 
init()
flip()

SURFACE
Es utilizado para representar una imagen o combinacion de imagenes en la pantalla
es uno de los principales servicios con los cuales se interactua

SPRITE
pueden representarse como los actores del juego
clase base para representar objetos
vienen con una gran cantidad de metodos con los cuales pueden interactuar con el ambiente del juego

GRUPOS 
Clase contenedora de sprites
Define comportamientos msd especificos para sprites

RECT
Representacion de bajo nivel de objetos como los sprites
define y controla ares en l pantalla
el espacio que van a usar los objetos o los personajes del juego

MIXER
La manera en la que el programador implementa los efectos de sonido y musica dentro del juego

pygame solo puede crear juegos en os dimensiones


el __main__.  sirve para saber si estas en el flujo principal 
"""
import pygame, sys
from pygame.locals import *

WIDTH = 640
HEIGHT = 480

def main():
	screen = pygame.display.set_mode((WIDTH,HEIGHT))
	#NOMBRE DE NUESTRA VENTANA
	pygame.display.set_caption("Prueba pygame")

	while True:
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)

	return 0

if __name__ == '__main__':
	pygame.init() #para inicializar pygame, va sir¡empre antes de llamar al main
	main()

