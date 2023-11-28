def separar_digitos(numero):
    digitos = []
    while numero > 0:
        digito = numero % 10
        digitos.insert(0, digito)
        numero = numero // 10
    return digitos

n = int(input("Ingrese un número entero: "))
resultado = separar_digitos(n)
print("Dígitos separados:", resultado)