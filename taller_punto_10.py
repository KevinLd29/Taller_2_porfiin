def multiplesDeTres(lista):
    # Con comprensión de listas
    multiplesComprension = [num for num in lista if sum(int(digito) for digito in str(num)) % 3 == 0]

    # Con patrón de acumulación
    multiplesAcumulacion = []
    for num in lista:
        if sum(int(digito) for digito in str(num)) % 3 == 0:
            multiplesAcumulacion.append(num)

    return multiplesComprension, multiplesAcumulacion

# Ejemplo de uso
listaA = [123, 45, 678, 9, 333]
resultadoComprension, resultadoAcumulacion = multiplesDeTres(listaA)

print("Multiplos de 3 (comprensión):", resultadoComprension)
print("Multiplos de 3 (acumulación):", resultadoAcumulacion)
