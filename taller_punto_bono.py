def esMatrizMagica(matriz):
    # Verificar filas y columnas
    sumaFila = sum(matriz[0])
    sumaColumna = sum(fila[0] for fila in matriz)

    if any(sum(fila) != sumaFila for fila in matriz) or any(sum(fila[i] for fila in matriz) != sumaColumna for i in range(len(matriz))):
        return False

    # Verificar diagonales
    diagonalPrincipal = sum(matriz[i][i] for i in range(len(matriz)))
    diagonalSecundaria = sum(matriz[i][len(matriz) - 1 - i] for i in range(len(matriz)))

    return diagonalPrincipal == diagonalSecundaria == sumaFila

# Ejemplo de uso
matrizEjemplo = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

if esMatrizMagica(matrizEjemplo):
    print("La matriz es mágica.")
else:
    print("La matriz no es mágica.")
