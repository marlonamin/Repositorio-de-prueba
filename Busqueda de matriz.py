matriz = [
    [4, 5, 9],
    [2, 7, 0],
    [1, 3, 8]
]
valor_buscado = 2

fila_encontrada = -1
columna_encontrada = -0

# Recorrer la matriz para poder encontrar el valor:
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] ==valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break
    if fila_encontrada != -1:
        break
# Verificar si se encontró el valor y ver la posición
if fila_encontrada != -1:
    print(f"El valor {valor_buscado} se encontro en la fila {fila_encontrada} y columna {columna_encontrada}")
else:
    print(f"{valor_buscado} no se encontró en la matriz")