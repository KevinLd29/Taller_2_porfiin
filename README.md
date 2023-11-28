# Taller 2, por fin se hizo 

# 1. **Separar dígitos de un número entero:**
Este programa toma un número entero y utiliza operaciones como módulo y división entera para descomponerlo en sus dígitos individuales. Luego, estos dígitos se almacenan en una lista.

```python
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
````

# 2. **Separar parte entera y decimal de un número flotante:**
El programa recibe un número flotante y lo divide en dos partes: la parte entera (los dígitos antes del punto decimal) y la parte decimal (los dígitos después del punto decimal). Estos componentes se almacenan en listas separadas.

```python
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

````

# 3. **Números espejos:**
Dados dos números enteros, este programa verifica si son "números espejos", es decir, si al escribir uno de ellos de izquierda a derecha y el otro de derecha a izquierda, obtienes los mismos números.

```python
def sonNumerosEspejos(a, b):
    return str(a) == str(b)[::-1] and str(b) == str(a)[::-1]

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if sonNumerosEspejos(num1, num2):
    print("Los números son espejos.")
else:
    print("Los números no son espejos.")

````

# 4. **Aproximación de la función coseno con la serie de Taylor:**
El programa calcula una aproximación del coseno de un número utilizando la serie de Taylor. La aproximación se mejora al sumar más términos de la serie.

```python
import math

def aproximacionCoseno(x, n):
    resultado_aproximado = 0
    for i in range(n):
        resultado_aproximado += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    return resultado_aproximado

xValor = float(input("Ingrese el valor de x para calcular cos(x) alrededor de 0: "))
nTerminos = int(input("Ingrese el número de términos para la aproximación: "))

cosenoAproximado = aproximacionCoseno(xValor, nTerminos)
cosenoReal = math.cos(xValor)

print(f"Aproximación de cos({xValor}): {cosenoAproximado}")
print(f"Cos({xValor}) real: {cosenoReal}")
print(f"Diferencia: {abs(cosenoReal - cosenoAproximado)}")

````

# 5. **Mínimo Común Múltiplo (MCM) de dos números enteros:**
Utilizando el Algoritmo de Euclides, este programa encuentra el Mínimo Común Múltiplo (MCM) de dos números enteros, que es el menor número que es múltiplo de ambos.

```python
def mcmIterativo(a, b):
    def mcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return abs(a * b) // mcd(a, b)

def mcmRecursivo(a, b):
    def mcd(a, b):
        if b == 0:
            return a
        return mcd(b, a % b)

    return abs(a * b) // mcd(a, b)

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

mcm_iter = mcmIterativo(num1, num2)
mcm_rec = mcmRecursivo(num1, num2)

print(f"MCM (iterativo) de {num1} y {num2}: {mcm_iter}")
print(f"MCM (recursivo) de {num1} y {num2}: {mcm_rec}")

# AYUDA, no funcionó como quería xd

````

# 6. **Verificar elementos repetidos en una lista:**
Este programa determina si hay elementos repetidos en una lista, utilizando la propiedad de los conjuntos que no permiten duplicados. Si la longitud de la lista cambia después de convertirla a conjunto y luego volver a lista, significa que había duplicados.

```python
def hayElementosRepetidos(lista):
    return len(lista) != len(set(lista))

miLista = [1, 2, 3, 4, 5, 1]  # Puedes cambiar esta lista según tus necesidades
if hayElementosRepetidos (miLista):
    print("La lista tiene elementos repetidos.")
else:
    print("La lista no tiene elementos repetidos.")

````

# 7. **Buscar cadena con dos o más vocales en una lista:**
El programa busca en una lista de cadenas para encontrar la primera cadena que contiene al menos dos vocales. Utiliza una función para contar las vocales en cada cadena.

```python
def tieneVocales(cadena):
    vocales = "aeiouAEIOU"
    contadorVocales = sum(1 for letra in cadena if letra in vocales)
    return contadorVocales >= 2

listaCadenas = ["Hola", "Python", "Murciélago", "Gato"]  # Puedes cambiar esta lista según tus necesidades
cadenaConVocales = None

for cadena in listaCadenas:
    if tieneVocales(cadena):
        cadenaConVocales = cadena
        break

if cadenaConVocales:
    print(f"La primera cadena con dos o más vocales es: {cadenaConVocales}")
else:
    print("No existe una cadena con dos o más vocales en la lista.")

````

# 8. **Elementos de la primera lista que no están en la segunda lista:**
Este programa encuentra los elementos en la primera lista que no están presentes en la segunda lista, utilizando la comprensión de listas para crear una lista de elementos no comunes.

```python
def elementosNoComunes(lista1, lista2):
    return [elemento for elemento in lista1 if elemento not in lista2]

lista1 = [1, 'Hola', -12.3, True]
lista2 = [11, -12.3, 'Hola', False]

resultado = elementosNoComunes(lista1, lista2)
print("Elementos en la primera lista que no están en la segunda:", resultado)

````

# 9. **Punto del taller que no hice**
En este programa usamos el punto del taller 1, que fue el punto 7 que en ese momento no pude darle solución jaja, pero ahora con muchas mas herramientas a mi disposición, si se pudo, es hacerlo con vectores

```python
import statistics

# Función para calcular el promedio multiplicativo
def promedio_multiplicativo(numeros):
    multiplicacion = 1
    for num in numeros:
        multiplicacion *= num
    return multiplicacion ** (1 / len(numeros))

# Función principal
def main():
    numeros = []
    for i in range(5):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)

    # Calcular promedio
    promedio = sum(numeros) / len(numeros)
    print(f"Promedio: {promedio}")

    # Calcular mediana
    mediana = statistics.median(numeros)
    print(f"Mediana: {mediana}")

    # Calcular promedio multiplicativo
    promedio_mult = promedio_multiplicativo(numeros)
    print(f"Promedio Multiplicativo: {promedio_mult}")

    # Ordenar de forma ascendente
    ascendente = sorted(numeros)
    print(f"Números Ordenados Ascendente: {ascendente}")

    # Ordenar de forma descendente
    descendente = sorted(numeros, reverse=True)
    print(f"Números Ordenados Descendente: {descendente}")

    # Calcular potencia del mayor al menor
    potencia = descendente[0] ** ascendente[0]
    print(f"Potencia del Mayor al Menor: {potencia}")

    # Calcular raíz cúbica del menor número
    raiz_cubica = ascendente[0] ** (1 / 3)
    print(f"Raíz Cúbica del Menor Número: {raiz_cubica}")

if __name__ == "__main__":
    main()
````

# 10. **Filtrar múltiplos de 3 en una lista:**
La función toma una lista de números y filtra aquellos que son múltiplos de 3. Se realiza utilizando tanto comprensión de listas como un patrón de acumulación.

```python
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

````

# 11. **Verificar si una matriz es mágica:**
El programa determina si una matriz cuadrada es "mágica", lo cual significa que la suma de cada fila, columna y diagonal es igual. Verifica estas sumas para determinar si la matriz cumple con esta propiedad.

```python
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

````

Como siempre. agradezco su atención y espero que se haya aprendido algo:D

