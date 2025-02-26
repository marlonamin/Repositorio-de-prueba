def bubble_sort(lista):
#Ordena la lista en orden ascendente usando el algoritmo Bubble Sort.
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def main():
# Definir la matriz 3x3 con valores numéricos
    matriz = [
        [9, 3, 5],
        [4, 7, 1],
        [6, 8, 2]
    ]

# Mostrar la matriz original
    print("Matriz original:")
    for fila in matriz:
        print(fila)

# Ordenar todas las filas de la matriz
    for i in range(len(matriz)):
        matriz[i] = bubble_sort(matriz[i])

# Mostrar la matriz con todas las filas ordenadas
    print("\nMatriz con todas las filas ordenadas en orden ascendente:")
    for fila in matriz:
        print(fila)


if __name__ == "__main__":
    main()
