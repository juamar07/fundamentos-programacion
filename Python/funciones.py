def mostrar_mayor(v1,v2,v3):
    print("El valor mayor de los tres numeros es: ")
    if v1 > v2 and v1 > v3:
        print(v1)
    else:
        if v2 > v3:
            print(v2)
        else:
            print(v3)



def mostrar_menor(v1,v2,v3):
    print("El valor menor de los tres numeros es: ")
    if v1 < v2 and v1 < v3:
        print(v1)
    else:
        if v2 < v3:
            print(v2)
        else:
            print(v3)

def ordenar_mayor (v1,v2,v3):
    print("Los numero ordenados de mayor a menor son: ")
    for x in range(4):
        if ordenar_mayor[x]>ordenar_mayor[x+1]:
            mostrar_decen = ordenar_mayor[x]
            ordenar_mayor[x]=ordenar_mayor[x+1]
            ordenar_mayor[x+1]=mostrar_decen

def ordenar_menor (v1,v2,v3):
    print("Los numero ordenados de mayor a menor son: ")
    for x in range(4):
        if ordenar_menor[x]>ordenar_menor[x+1]:
            mostrar_acen = ordenar_menor[x]
            ordenar_menor[x]=ordenar_menor[x+1]
            ordenar_menor[x+1]=mostrar_acen


def cargar ():
    valor1= int (input ("Ingrese el primer valor:"))
    valor2 = int (input ("Ingrese el segundo valor:"))
    valor3 =int (input ("Ingrese el tercer valor:"))
    mostrar_mayor (valor1, valor2, valor3)
    mostrar_menor (valor1, valor2, valor3)
    ordenar_mayor (valor1, valor2, valor3)
    ordenar_menor (valor1, valor2, valor3)

cargar()