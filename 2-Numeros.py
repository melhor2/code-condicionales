print("Puedes digitar un numero y te decimos si es par o impar y si es negativo o positivo el numero")

Num1=int(input("Digite su numero : \n"))
if Num1%2==0 and Num1>0:
    print("El numero es par y positivo")
elif Num1%2==0 and Num1<0:
    print("El numero es par y negativo")
elif Num1%2!=0 and Num1 >0:
    print("El numero es impar y positivo")
elif Num1%2!=0 and Num1<0:
    print("El numero es impar y negativo")
else : print("El numero es igual a 0")