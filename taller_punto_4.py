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
