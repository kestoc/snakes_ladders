"""
    Autor: Kevin Steven Ocampo Morales

    Fecha: 10/7/2022

    Descripción: Este archivo contiene la logica del juego 'Escaleras y serpientes' que se solicita en la prueba técnica
    de la compañia VeeVart.

    Version: 1.0
"""

import random
from sys import stdin

snake , ladders = {}, {}

def throwDice():
    """
        Variables: Ninguna.

        Descripción: Función que retorna un valor aleatorio entre 1 y 6 para el dado del juego.
    """
    return random.randint(1,6)

def genMessage(num):
    assert(type(num) == int)
    assert(num >= 1 and num <= 5)
    """
    """
    ans = None

    match num:
        case 1:
            ans = "Jugador llega al cuadro"
        case 2:
            ans = "Jugador supera el cuadro"
        case 3:
            ans = "Jugador avanza a cuadro"
        case 4:
            ans = "Jugador desciende al cuadro"
        case 5:
            ans = "Jugador sube por la escalera al cuadro"
        case _:
            ans = "Codigo invalido."

    return ans

def game(n):
    assert(type(n) == int)
    assert(type(snake) == dict)
    assert(type(ladders) == dict)
    #assert(len(snake) <= (n*n-n)-1) #Asumiendo de que se llenan todas las casillas con serpientes desde la segunda fila hasta la ultima a excepcion de la casilla meta 
    #assert(len(ladders) <= n*n-n) #Asumiendo de que se llenan todas las casillas con escaleras desde la primera fila hasta la penultima fila
    """
        Variables: n que ser el tamaño del tablero de juego, quedando un total de n*n casillas.

        Descripcion: Función principal de ejecución del juego 'Escaleras y serpientes'.
    """
    value = 0
    while value < n*n:
        aux = throwDice()
        print("Dado arroja",aux)
        value += aux

        if value == n*n:
            print(genMessage(1),n*n)
            return
        elif value > n*n:
            print(genMessage(2),n*n)
            return

        print(genMessage(3), value)

        if value in snake:
            value = snake[value]
            print(genMessage(4), value)

        elif value in ladders:
            value = ladders[value]
            print(genMessage(5), value)

def main():
    """
        Variables: Ninguna.

        Descripción: Función principal para solicitar los datos para el juego. Se solicita n que es el tamaño del tablero
        s que seran las ubicaciones de las serpientes y a donde se desciende y l que seran las ubicaciones de las escaleras y
        a donde se asciende.
    """

    n = int(input("Ingrese el tamaño del tablero: "))

    print("\nIngrese la casilla donde estara la serpiente y seguido, la casilla a la que desciende al caer en ella (separado por espacios): ")
    s = list(map(int,stdin.readline().split()))
    
    for i in range(1,len(s),2):
        if s[i-1] >= n*n or s[i] >= n*n:
            print("Valores invalidos.")
            return
        snake[s[i-1]] = s[i]

    print("\nIngrese la casilla donde estara la escalera y seguido, la casilla a la que asciende al caer en ella (separado por espacios): ")
    l = list(map(int,stdin.readline().split()))
    
    for i in range(1,len(l),2):
        if l[i-1] >= n*n or l[i] >= n*n:
            print("Valores invalidos.")
            return
        ladders[l[i-1]] = l[i]
   
    game(n)
    print("Fin")

main()