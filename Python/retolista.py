# Ejercicio que genera numeros aleatorios y pide al usuario que ingrese una valor y confirmar si esta dentro de los numeros random generados 

leer_valor = 0 

lista=[]
lista1=[]

import random

for x in range (8):

    aleatorio = random.randint(1,4)
    print()
    leer_valor = int(input("Ingrese un numero entero positivo: "))
    

    if leer_valor == aleatorio:
        numold = leer_valor
        lista1.append(leer_valor)
        lista1.sort()
        aleatorio_1 = [aleatorio]
        numnew = -1
        index = [aleatorio].index(numold)
        aleatorio = [aleatorio]
        aleatorio[index] = numnew
        lista.append(aleatorio)
        print(f"El numero se encuntra en la lista y es: {aleatorio_1}")

    elif leer_valor > aleatorio:
        print("El numero no se encuentra en la lista")
    elif leer_valor < aleatorio:
        print("El numero no se encuentra en la lista")
        
print()
print(f"la lista con el -1 es: {lista} y la lista sin el -1: {lista1}")
print()
print(f"Hay {len(lista1)} numeros en la lista")
print()
print(f"El numero 1 se repite {lista1.count(1)} veces, el numero 2 se repite {lista1.count(2)} veces, el numero 3 se repite {lista1.count(3)} veces")
print()