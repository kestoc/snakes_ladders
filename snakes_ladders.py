"""
    Autor: Kevin Steven Ocampo Morales

    Fecha: 10/7/2022

    Descripción: Este archivo contiene la logica del juego 'Escaleras y serpientes' que se solicita en la prueba técnica
    de la compañia VeeVart.

    Version: 1.0
"""

import random
from sys import stdin

def throwDice():
    """
        Variables: Ninguna.

        Descripción: Función que retorna un valor aleatorio entre 1 y 6 para el dado del juego.
    """
    return random.randint(1,6)


def game(n,s,l):
    assert(type(n) == int)
    assert(type(s) == dict)
    assert(type(l) == dict)
    assert(len(s) <= (n*n-n)-1) #Asumiendo de que se llenan todas las casillas con serpientes desde la segunda fila hasta la ultima a excepcion de la casilla meta 
    assert(len(l) <= n*n-n) #Asumiendo de que se llenan todas las casillas con escaleras desde la primera fila hasta la penultima fila
    """
        Variables: n que ser el tamaño del tablero de juego, en este caso sera siempre 5 para tener un tablero de 5x5 o lo que es igual
        un tablero de 25 casillas en total.

        Descripcion: Función principal de ejecución del juego 'Escaleras y serpientes'.
    """
    value = 0 ; snake = s ; ladders = l
    while value < n*n:
        aux = throwDice()
        print("Dado arroja",aux)
        value += aux

        if value == n*n:
            print("Jugador llega al cuadro",n*n)
            print("Fin")
            return
        elif value > n*n:
            print("Jugador supera el cuadro",n*n)
            print("Fin")
            return

        print("Jugador avanza al cuadro", value)

        if value in snake:
            value = snake[value]
            print("Jugador desciende al cuadro", value)

        elif value in ladders:
            value = ladders[value]
            print("Jugador sube por escalera al cuadro", value)

def main():
    """
        Variables: Ninguna.

        Descripción: Función principal para solicitar los datos para el juego.
    """
    newS, newL = {}, {}

    n = int(input("Ingrese el tamaño del tablero: "))

    print("\nIngrese la casilla donde estara la serpiente y seguido, la casilla a la que desciende al caer en ella (separado por espacios): ")
    snake = list(map(int,stdin.readline().split()))
    
    for i in range(1,len(snake),2):
        if snake[i-1] >= n*n or snake[i] >= n*n:
            print("Valores invalidos.")
            return
        newS[snake[i-1]] = snake[i]

    print("\nIngrese la casilla donde estara la escalera y seguido, la casilla a la que asciende al caer en ella (separado por espacios): ")
    ladders = list(map(int,stdin.readline().split()))
    
    for i in range(1,len(ladders),2):
        if snake[i-1] >= n*n or snake[i] >= n*n:
            print("Valores invalidos.")
            return
        newL[ladders[i-1]] = ladders[i]
   
    game(n,newS,newL)

main()