def separarPartes(n):
    # Convertir el número a una cadena de texto
    nStr = str(n)
    
    # Separar la parte entera y decimal
    partes = nStr.split('.')
    
    # Obtener la parte entera y decimal como enteros
    parteEntera = int(partes[0])
    parteDecimal = int(partes[1])
    
    # Obtener los dígitos de la parte entera y decimal
    digitosEntera = [int(digito) for digito in str(parteEntera)]
    digitosDecimal = [int(digito) for digito in str(parteDecimal)]
    
    return digitosEntera, digitosDecimal

# Solicitar al usuario que introduzca un número
n = float(input("Por favor, introduce un número: "))

# Llamar a la función con el número introducido por el usuario
entera, decimal = separarPartes(n)

# Imprimir los resultados
print("Dígitos de la parte entera:", entera)
print("Dígitos de la parte decimal:", decimal)
