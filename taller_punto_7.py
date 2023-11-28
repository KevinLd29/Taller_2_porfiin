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
