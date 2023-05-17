# Programa para cacular nota de parcial por estudiante y por el grupo 
print()
# inicializacion de variables 
c_valexateo = 0.40 
c_valesapra = 0.60
V_concic = 1
v_sumnotpripar = 0
v_notproest = 1 
v_prom = 0

# Leer cantidad de estudiantes 
v_cantest = int(input("Digite la cantidad de estudiantes: "))
print()

for v_concic in range (v_cantest):
   
    # Captura de datos

   v_nomest = input ("Nombre del estudiante: ")
   v_genest = input ( "Genero del estudiante, si es hombre escirba 1 y si es mujer escriba 2: ")
   v_notexateo = float(input("Digite la nota del examen teorico: "))
   v_notexapra = float(input("Digite la nota del examen practico: "))
   print()

   # Calculo de nota del primer parcial por estudiante 

   v_notdefpripar = (v_notexateo * c_valexateo) + (v_notexapra * c_valesapra)
   v_notdefexapra = (v_notexapra * c_valesapra)
   v_notdefexateo = (v_notexateo * c_valexateo)

   print(f"{v_nomest}, Su nota del primer parcial es: {v_notdefpripar:.2f}")
   print()

   # Calcula suma de las notas de todos los estudiantes 
   v_sumnotpripar = v_sumnotpripar + v_notdefpripar
   print("La sumatoria de todas las notas de los estudiantes es: ",v_sumnotpripar)

# calcular promedio del grupo de las notas del primer parcial 
v_pronotpripar = v_sumnotpripar / v_cantest
print(f"El promedio del grupo del primer parcial es: {v_pronotpripar:.2f}")

# Calcular promedio por parte del parcial   
v_pronotpripra = v_notdefexapra / v_cantest
print(f"El promedio del grupo del primer parcial practico es: {v_pronotpripra:.2f}")

v_pronotpriteo = v_notdefexateo / v_cantest
print(f"El promedio del grupo del primer parcial teorico es: {v_pronotpriteo:.2f}")
print()

# Calcular promedio por genero 

if v_genest == 2:
  print

elif v_genest == 1:
   print

else:
   print("Se equivoco de genero")

for v_notdefpripar in v_cantest:
   v_prom += v_notdefpripar
   print("El promedio del grupo del primer parcial es: ",v_prom)

v_notdeflist1 = list(v_notdefpripar)

minimo = min(v_notdeflist1)
maximo = max(v_notdeflist1)

print("La nota minima del primer parcial es:", minimo )
print("La nota max del primer parcial es:", maximo)
