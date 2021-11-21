# -*- coding: utf-8 -*-
#
# autor: Hugo Ruscitti
# web: www.losersjuegos.com.ar
# licencia: GPL 2

import pygame
from pygame.locals import *
from pygame import mixer
from principal import *


class Menu:
    pygame.mixer.init()
    pygame.mixer.music.load("menumusic.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()    

    def __init__(self, opciones):
        self.opciones = opciones
        self.font = pygame.font.Font('font.ttf', 20)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:

                # Invoca a la función asociada a la opción.
                titulo, funcion = self.opciones[self.seleccionado]
                funcion()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]


    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        total = self.total
        indice = 0
        altura_de_opcion = 50
        x = 105
        y = 105
        
        for (titulo, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = (200, 0, 0)
            else:
                color = (0, 0, 0)

            imagen = self.font.render(titulo, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)

def salir_del_programa():
    import sys
    print ("Gracias por jugar!")
    sys.exit(0)

def iniciar_facil():
    main(1)

def iniciar_normal():
    main(2)

def iniciar_dificil():
    main(3)

if __name__ == '__main__':

    dificultad = [1,2,3]
    salir = False
    opciones = [
        ("Facil", iniciar_facil),
        ("Normal", iniciar_normal),
        ("Dificil", iniciar_dificil),
        ("Salir", salir_del_programa)
        ]

    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    fondo = pygame.image.load("bgmenu.jpg").convert()
    menu = Menu(opciones)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)