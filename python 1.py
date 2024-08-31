def buscar_valor_en_matriz(matriz, valor):
    """
    Busca un valor en una matriz bidimensional y retorna la posición si se encuentra.

    :param matriz: Lista de listas que representa la matriz bidimensional.
    :param valor: Valor a buscar en la matriz.
    :return: Tupla con la posición (fila, columna) si el valor se encuentra, de lo contrario None.
    """
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor:
                return (fila, columna)
    return None


# Definir la matriz 3x3
matriz_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar en la matriz
valor_a_buscar = 5

# Realizar la búsqueda
resultado = buscar_valor_en_matriz(matriz_3x3, valor_a_buscar)

# Mostrar el resultado
if resultado:
    print(f"El valor {valor_a_buscar} se encontró en la posición: {resultado}")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")