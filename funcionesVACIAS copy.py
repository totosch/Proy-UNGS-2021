from configuracion import *

import random
import math

def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    
    palabra_azar = random.choice(lista)
    espacio_entre_letrasuno = 20
    espacio_entre_letrasdos = 280
    espacio_entre_letrastres = 550
    eje_y = 40
    
    for char in palabra_azar:
        numero = random.randint(1,3)
        if numero == 1:
                listaIzq.append(char)                
        if numero == 2:
                listaMedio.append(char)
        if numero == 3:
                listaDer.append(char)

        for i in listaIzq:
            posicionesIzq.append([espacio_entre_letrasuno,eje_y])
            posicionesIzq.append([eje_y])
        for i in listaMedio:
            posicionesMedio.append([espacio_entre_letrasdos])
            posicionesMedio.append([eje_y])
        for i in listaDer:
            posicionesDer.append([espacio_entre_letrastres])
            posicionesDer.append([eje_y])

#elige una palabra de la lista y la carga en las 3 listas
# y les inventa una posicion para que aparezca en la columna correspondiente


def bajar(lista, posiciones):
    indices = []
    for i in range(len(posiciones)):
        pos = posiciones[i]
        pos[1] += 35
        if len(lista) > 0 and pos[1] >= 510:
            indices.append(i)
    indices.reverse()
    for i in indices:
        lista.pop(i)
        posiciones.pop(i)



def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    bajar(listaIzq, posicionesIzq), bajar(listaDer, posicionesDer), bajar(listaMedio, posicionesMedio)       
    cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)

def estaCerca(elem, lista):
    #es opcional, se usa para evitar solapamientos
    pass

def Puntos(candidata):
    candidata = ""
    un_punto = ["a", "e", "i", "o", "u"]
    dos_puntos = ["b","c","d","f","g","h","l","m","n","p","r","s","t","v"]
    cinco_puntos = ["j","k","q","w","x","y","z"]
    puntaje = 0

    for i in candidata:
        if i in un_punto:
            puntaje += 1
        elif i in dos_puntos:
            puntaje += 2
        elif i in cinco_puntos:
            puntaje += 5
        return puntaje
    #devuelve el puntaje que le corresponde a candidata

def procesar(lista, candidata, listaIzq, listaMedio, listaDerecha):
    if candidata in lista:
        Puntos(lista)
    if candidata not in lista:
        return 0
    #chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta
    pass


def esValida(lista, candidata, listaIzq, listaMedio, listaDerecha):
    #devuelve True si candidata cumple con los requisitos
    pass