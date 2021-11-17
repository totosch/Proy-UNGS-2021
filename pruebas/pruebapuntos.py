def Puntos(candidata):

    un_punto = ["a", "e", "i", "o", "u"]
    dos_puntos = ["b","c","d","f","g","h","i","l","m","n","p","r","s","t","v"]
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
    pass

print(Puntos("benju"))