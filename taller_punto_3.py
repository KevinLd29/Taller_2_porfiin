def sonNumerosEspejos(a, b):
    return str(a) == str(b)[::-1] and str(b) == str(a)[::-1]

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if sonNumerosEspejos(num1, num2):
    print("Los números son espejos.")
else:
    print("Los números no son espejos.")
