def elementosNoComunes(lista1, lista2):
    return [elemento for elemento in lista1 if elemento not in lista2]

lista1 = [1, 'Hola', -12.3, True]
lista2 = [11, -12.3, 'Hola', False]

resultado = elementosNoComunes(lista1, lista2)
print("Elementos en la primera lista que no están en la segunda:", resultado)
