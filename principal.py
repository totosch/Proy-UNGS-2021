import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *
from menu import *
from pygame import mixer

#Funcion principal

def main(dificultad):

        #dificultad = 3 #int(input("DIFICULTAD?\n1: FACIL\n2: NORMAL\n3: EXPERTO\n"))
        #if dificultad not in [1,2,3]:
        #    print("Dificultad incorrecta")
        #    main()
        #    return
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()
        pygame.mixer.music.load("musica.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

        pygame.display.set_caption("Insomniac!")
        screen = pygame.display.set_mode((800, 600))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        highscore = 0
        candidata = ""
        listaIzq = []
        listaMedio = []
        listaDer = []
        posicionesIzq = []
        posicionesMedio = []
        posicionesDer = []
        lista = []

        archivo = open("lemario.txt","r")
        for linea in archivo.readlines():
            lista.append(linea[0:-1])
        
        highscore_file = open("highscore.txt","r")
        highscore = int(highscore_file.read())
        


        cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)
        dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos, highscore)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = dificultad
            
            if puntos > highscore:
                writehighscore = open("highscore.txt","w")
                highscore = puntos
                writehighscore.write(str(highscore))
            

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(lista, candidata, listaIzq, listaMedio, listaDer)
                        candidata = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000
            
            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos,highscore)

            pygame.display.flip()

            actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq,
                posicionesMedio, posicionesDer)

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
