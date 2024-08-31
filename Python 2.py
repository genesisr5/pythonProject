def bubble_sort(arr):
    """
    Ordena un arreglo en orden ascendente usando el algoritmo de Bubble Sort.

    :param arr: Lista de números a ordenar.
    :return: La lista ordenada.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambiar los elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def ordenar_fila(matriz, fila_index):
    """
    Ordena una fila específica de la matriz usando Bubble Sort.

    :param matriz: Lista de listas que representa la matriz bidimensional.
    :param fila_index: Índice de la fila a ordenar.
    :return: La matriz con la fila especificada ordenada.
    """
    if 0 <= fila_index < len(matriz):
        matriz[fila_index] = bubble_sort(matriz[fila_index])
    else:
        print(f"Índice de fila {fila_index} fuera de rango")
    return matriz


# Definir la matriz 3x3
matriz_3x3 = [
    [9, 2, 7],
    [4, 5, 6],
    [1, 8, 3]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz_3x3:
    print(fila)

# Fila a ordenar (por ejemplo, la fila con índice 0)
fila_a_ordenar = 0

# Ordenar la fila
matriz_ordenada = ordenar_fila(matriz_3x3, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz después de ordenar la fila:")
for fila in matriz_ordenada:
    print(fila)
