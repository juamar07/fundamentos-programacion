# 5.1 - Leer por teclado un número que represente una cantidad de números que a su vez se leerán también por teclado.
# Calcular la suma de todos esos números.

suma = 0
print()
while True: 

   total = int(input("ingrese la cantidad e veces a repetir: "))
   
   for x in range(total):

      numero = int(input("ingrese un numero: "))
      suma += numero
      x -= 1
      print (f"La suma de los {numero} numeros es: {suma}")
   if total > 0:
     break
print()

# 5.2 - Contar los números enteros positivos introducidos por teclado. 
# Se consideran dos variables enteras numero y contador (contará el número de enteros positivos). 
# Se supone que se leen números positivos y se detiene el bucle cuando se lee un número negativo o cero.

while True:

   num = int(input("ingrese un numero: "))

   if num > 0:
      print("Numero positivo")
      print()

   elif num <= 0:
      print()
      print("Ha digitado cero o un numero negativo")
      print()
      break 



   


