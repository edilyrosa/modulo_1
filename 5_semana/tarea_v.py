texto = input("Ingresa una palabra o frase: ")

vocales = "aeiouAEIOU"
contador_vocales = 0
contador_caracteres = 0

for caracter in texto:
    contador_caracteres += 1
    
    if caracter in vocales:
        contador_vocales += 1

print("Número de vocales:", contador_vocales)
print("Número de caracteres:", contador_caracteres)