print("Escribe una palabra o una frase ")
print("El programa te va a saleccionar solo las vocales")
lista=input("Ingrese la palabra o la frase: \n") .lower()
for cadena in lista:
    for caracter in cadena :
        vocales=caracter.lower()
        if vocales in "aeiou":
            print(vocales)
print("Fin del programa")