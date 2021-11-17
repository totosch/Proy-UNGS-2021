from pygame import mixer
from configuracion import *

import random
import math

palabras = []

def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    
    palabra_azar = random.choice(lista)
    global palabras
    palabras.append(palabra_azar)

    col0 = 0
    col1 = 0
    col2 = 0
    ancho_columna = 260
    offset_x = 20
    eje_y = 40
    espacio_entre_letras = 20
    
    for char in palabra_azar:
        numero = random.randint(0,2)
        if numero == 0:
                posicionesIzq.append([offset_x + ancho_columna*numero + col0*espacio_entre_letras,eje_y])
                listaIzq.append(char)
                col0 += 1               
        if numero == 1:
                posicionesMedio.append([offset_x + ancho_columna*numero + col1*espacio_entre_letras,eje_y])
                listaMedio.append(char)
                col1 += 1
        if numero == 2:
                posicionesDer.append([offset_x + ancho_columna*numero + col2*espacio_entre_letras,eje_y])
                listaDer.append(char)
                col2 += 1
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
    puntaje = 0
    un_punto = ["a", "e", "i", "o", "u"]
    dos_puntos = ["b","c","d","f","g","h","l","m","n","p","r","s","t","v"]
    cinco_puntos = ["j","k","q","w","x","y","z"]    

    for i in candidata:
        if i in un_punto:
            puntaje += 1
        elif i in dos_puntos:
            puntaje += 2
        elif i in cinco_puntos:
            puntaje += 5
    return puntaje
    
    #devuelve el puntaje que le corresponde a candidata

def procesar(lista, candidata, listaIzq, listaMedio, listaDer):
    global palabras
    for i in range(0,len(palabras)):
        if palabras[i] == candidata:
            sonido = mixer.Sound("sonido.wav")
            sonido.set_volume(0.3)
            sonido.play()
            palabras.pop(i)
        
            return Puntos(candidata)
    else:
        return 0
    #chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta

def esValida(lista, candidata, listaIzq, listaMedio, listaDer):  
    #devuelve True si candidata cumple con los requisitos
    pass