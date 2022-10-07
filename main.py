import snakes_ladders
from sys import stdin

def main():
    """
        Variables: Ninguna.

        Descripción: Función principal para solicitar los datos para el juego. Se solicita n que es el tamaño del tablero
        s que seran las ubicaciones de las serpientes y a donde se desciende y l que seran las ubicaciones de las escaleras y
        a donde se asciende.
    """

    n = int(stdin.readline().strip()) #Leo el tamaño del tablero

    s = list(map(int,stdin.readline().strip().split())) #Leo la lista de serpientes
    
    #Transformo la lista a un diccionario
    for i in range(1,len(s),2):
        if s[i-1] >= n*n or s[i] >= n*n: #Verifico que los valores sean validos dentro del tamaño del tablero
            print("Valores invalidos.")
            return -1
        snakes_ladders.snake[s[i-1]] = s[i]

    l = list(map(int,stdin.readline().strip().split())) #Leo la lista de escaleras
    
    #Transformo la lista a un diccionario
    for i in range(1,len(l),2):
        if l[i-1] >= n*n or l[i] >= n*n: #Verifico que los valores sean validos dentro del tamaño del tablero
            print("Valores invalidos.")
            return -1
        snakes_ladders.ladders[l[i-1]] = l[i]
   
    print(snakes_ladders.game(n)) #Se llama al juego para la ejecucion con los datos obtenidos
    return 0

main()