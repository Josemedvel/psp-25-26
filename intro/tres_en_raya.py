def construir_tablero(filas):
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(filas):
            fila.append('')
        tablero.append(fila)    
    return tablero

def imprimir_tablero(tablero):
    for fila in range(len(tablero)):
        if fila != 0:
                print("_" * (17*len(tablero)))
        for col in range(len(tablero[fila])):
            if col == 0:
                print("\t" + str(tablero[fila][col]), end="")
                print("\t|\t", end="")
            elif col != len(tablero) - 1:
                print(tablero[fila][col], end="")
                print("\t|\t", end="")
            else:
                print(tablero[fila][col])


tablero = construir_tablero(3)
imprimir_tablero(tablero)