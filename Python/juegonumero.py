# Juego adivina el numero

import random

aleatorio = random.randint(1,100)

print("\t .:Juego adivina el número:.")

contador = 0
while True:
    num = int(input("Digite un numero: "))
    contador += 1
    if num>aleatorio:
        print("\tNo es el el numero, digita un numero menor")
    elif num<aleatorio:
        print("\tNo es el el numero, digita un numero mayor")
    else:
        print(f"\tFelicidades, acabas de adivinar el número, el cual era el: {aleatorio}")
        continuar = input("Desea continuar jugando? ").lower
        
        if continuar == 'si':
            print()
        elif continuar == 'no':
            break

print(f"\nNumero de intentos: {contador}")