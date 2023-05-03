print("Escribe una palabra o una frase ")
print("El programa te va a saleccionar solo las consonantes")
lista=input("Ingrese la palabra o la frase: \n") .lower()
for cadena in lista:
    for caracter in cadena :
        consonantes=caracter.lower()
        if consonantes in "bcdfghjklmnñpqrstvwxyz":
            print(consonantes)
print("Fin del programa")