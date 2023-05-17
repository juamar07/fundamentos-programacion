# Listas 

# Ejercicio 1 
lista = []

for x in range (5):
    valor = int(input("Ingrese un valor entero: ")) # --> Asignacion
    lista.append(valor)
    
print(lista)
print(len(lista))

# Ejercicio 2 
lista1 = []

valor = int(input("Ingrese un valor (0 para finalizar): "))
while valor != 0:
    lista1.append(valor)
    valor = int(input("Ingrese un valor (0 para finalizar): "))

print(f"Tamaño de la lista: {len(lista1)}")

# Ejercicio 3 
mayor = lista1[0]
posicion = 0 
for y in range (1,5):
    if lista1 [y]>mayor:
        mayor = lista1[y]
        posicion = y

print(f"Lista completa: {lista1} y el mayor de la lista es: {mayor}")

menor = lista1[0]
posicion = 0 
for x in range (1,5):
    if lista1 [x]<menor:
        menor = lista1[x]
        posicion = x

print(f"Lista completa: {lista1} y el menor de la lista es: {menor}")

consulta = int(input("Digite el valor que desea buscar en la lista: "))
if consulta is lista1:
    print(f"El numero {consulta} si se encuentra en la lista")
else:
    print(f"El numero {consulta} no se encuentra en la lista")

# sueldo mayor y menor 

sueldo = []
for f in range (5):
    valor = int(input("ingrese el sueldo: "))
    sueldo.append(valor)
    

print(f"Lista de sueldo sin ordenar {sueldo}")
print(sueldo.sort())
conint = 0 

for f in range(4):
    if sueldo[f]>sueldo[f+1]:
        aux = sueldo[f]
        sueldo [f] = sueldo [f+1]
        sueldo[f+1] = aux 
        conint += 1

print (f"Lista con el ultimo elemento ordenado: {sueldo} y su canditad de intercmabios: {conint}")

# numero mayor y menor 

a = 4 
b = 7
c = 10

if a >= b and a >= c:
    print()
elif b >= a  and b >= c:
    print()
else:
    print()


    

