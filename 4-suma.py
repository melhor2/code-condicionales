print("Ingrese el numero : \n")
a = int(input())
b=0
for i in range (1,a+1):
    print(i)
    b=b+i
print("La suma es :" ,b)









print("Escriba los numeros de su lista")
n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())
n6=int(input())

lista=[n1,n2,n3,n4,n5,n6]

def sumar(lista):
    suma=0
    for elemento in lista:
        suma+=elemento
    return suma
print(sumar(lista))