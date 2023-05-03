comprobar=True

while comprobar ==True:
    n=int(input("Ingrese un numero entero positivo : "))

    if n > 0 :
        for i in range(1,11):
            print(n, "por", i, "=", n*i)
        comprobar= False
    else: print("El numero ingresado no es correcto, intentalo nuevamente")