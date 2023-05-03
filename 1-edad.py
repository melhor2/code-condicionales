print("Bienvenid a Cine Colombia")
print("¿Que pelicula quieres ver?")
print("Cartelera \n1-Evil Dead Rise: El despertar +18 \n2-Super Mario Bros. La palicula +9 ")
pelicula= input() .lower()
if pelicula== "1":
    print("¿Tienes la edad adecuada para ver esta pelicula?")
    mayor = int(input("Ingrese su edad porfavor: \n*"))
    if mayor >18 :
        print("Puedes ver la pelicula")
    else: print("No puedes ver esta pelicula")
elif pelicula=="2":
    print("¿Tienes la edad adecuada para ver esta pelicula?")
    menor = int(input("Ingrese su edad porfavor: \n*"))
    if menor >9 :
        print("Puedes ver este pelicula")
    else: print ("No puedes ver esta pelicula")
    

    
