"""
    Autor: Kevin Steven Ocampo Morales

    Fecha: 10/7/2022

    Descripción: Este archivo contiene la logica del juego 'Escaleras y serpientes' que se solicita en la prueba técnica
    de la compañia VeeVart.

    Version: 1.0
"""

import random

snake , ladders = {}, {} #Diccionarios que permiten almacenar la informacion de las serpientes y escaleras del juego actual

def throwDice():
    """
        Variables: Ninguna.

        Descripción: Función que retorna un valor aleatorio entre 1 y 6 para el dado del juego.
    """
    return random.randint(1,6)

def genMessage(num):
    assert(type(num) == int) ; assert(num >= 1 and num <= 4)
    """
        Variables: num que sera el codigo del mensaje a devolver.

        Descripcion: Función que retorna el mensaje a imprimir en consola
    """
    ans = None #Variable que almacena el mensaje a devolver

    match num:
        case 1: #Caso cuando se llega al final del juego
            ans = "Jugador llego o supero el cuadro"
        case 2: #Caso cuando se avanza a una casilla cualquiera (no tiene serpiente ni escalera)
            ans = "Jugador avanza a cuadro"
        case 3: #Caso cuando se cae en una casilla con serpiente
            ans = "Jugador desciende al cuadro"
        case 4: #Caso cuando se cae en una casilla con escalera
            ans = "Jugador sube por la escalera al cuadro"

    return ans

def state(n,val):
    global aux
    assert(type(n) == int) ; assert(n >= 1) ; assert(type(val) == int) ; assert(val >= 1)
    """
        Variables: n que es el tamaño del tablero
                   val que indica el valor de la casilla a la que me desplazare

        Descripcion: Función que permite verificar el estado del juego y saber asi que acción se debe mostrar ne pantalla
    """
    aux = val
    ans = genMessage(2),aux #Inicialmente se debe mostrar el mensaje de la casilla a la que se desplazara
    
    if aux >= n*n: #Si llegamos a la ultima casilla o la pasamos, mostramos esta ultima acción
        ans = genMessage(1),n*n 
    
    if aux in snake: #En caso de que caigamos en una serpiente, se muestra esta acción y se actualiza la casilla a la que cayó
        print(ans[0],ans[1])
        aux = snake[aux]
        ans = genMessage(3),aux
    
    if aux in ladders: #En caso de que caigamos en una escalera, se muestra esta acción y se actualiza la casilla a la que cayó
        print(ans[0],ans[1])
        aux = ladders[aux]
        ans = genMessage(4),aux
    
    return ans

def game(n):
    global value
    assert(type(n) == int) ; assert(n >= 1)
    """
        Variables: n que ser el tamaño del tablero de juego, quedando un total de n*n casillas.

        Descripcion: Función principal de ejecución del juego 'Escaleras y serpientes'.
    """
    value = 0 #Valor que indica la casilla actual
    
    #Mientras no llegue a la ultima casilla o me pase de ella, continuo jugando
    while value < n*n:
        aux = throwDice() #Lanzo el dado
        print("Dado arroja",aux)
        value += aux #Actualizo la casilla
        msg, total = state(n,value) #Consulto el estado del juego y por ende lo que se debe mostrar en pantalla
        print(msg, total)
    
    #Finaliza sin problemas el juego
    return "Fin"