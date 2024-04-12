import os


def limpiar_terminal():
    # Función para que se borre el terminal con cada imput
    os.system('cls' if os.name == 'nt' else 'clear')

laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
]
# Diccionario para traducir los imputs 
traduccionmovimientos = {"b":"abajo", "s": "subir", "d":"derecha", "i": "izquierda"}
movimientos = []

muros = set(((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3)))

posicion_jugador = 0
posicion_actual = (0, 0)
# Metodo para imprimir el laberinto
def imprimir_laberinto(posicion_jugador):
    for i, fila in enumerate(laberinto):
        for j, columna in enumerate(fila):
            if (i, j) == posicion_jugador:
                print('P', end=' ')
            elif (i, j) in muros:
                print('X', end=' ')
            else:
                print(columna, end=' ')
        print()

imprimir_laberinto(posicion_jugador)


    