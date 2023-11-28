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
