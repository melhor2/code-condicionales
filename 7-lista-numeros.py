print("Escriba los numeros de su 1ra lista")
n1=int(input())
n2=int(input())
n3=int(input())
print("Escriba los numeros de su 2da lista")
n4=int(input())
n5=int(input())
n6=int(input())

lista=[n1,n2,n3]
def sumar(lista):
    suma=0
    for elemento in lista:
        suma+=elemento
    return suma
print(sumar(lista))
lista2=[n4,n5,n6]
def sumar(lista2):
    suma=0
    for elemento in lista2:
        suma+=elemento
    return suma
print(sumar(lista2))
#sumar(lista , lista2 )
sumar(lista)
sumar(lista2)
print("Resultados de las 2 listas")
print(f"Lista 1 : {lista}",sumar(lista))
print(f"Lista 2 : {lista2}",sumar(lista2))