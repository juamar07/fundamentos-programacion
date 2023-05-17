# Programa para cacular nota de parcial por estudiante y por el grupo 
print()

# inicializacion de variables 
v_cantest = 0
c_valexateo = 0.40 
c_valesapra = 0.60
v_defpripra = 0.0 
V_concic = 1
v_pronotpripar = 0
v_sumnotpripar = 0
v_prom = 0
acusumdem = 0
acusumdeh = 0
acucantestm = 0
acucantesth = 0
v_notmaxm = 5.1
v_notminm = 0.0
v_notmaxh = 5.1
v_notminh = 0.0  
v_pronotparm = 0
v_pronotparh = 0

# Leer cantidad de estudiantes 
v_cantest = int(input("Digite la cantidad de estudiantes: "))

for v_concic in range (v_cantest):

   # Captura de datos

   v_nomest = input ("Nombre del estudiante: ")
   v_genEst = input ( "Genero del estudiante, si es hombre escirba 1 y si es mujer escriba 2: ")
   v_notexateo = float(input("Digite la nota del examen teorico: "))
   v_notexapra = float(input("Digite la nota del examen practico: "))
   
   # Calculo de nota del primer parcial por estudiante 
   v_notdefpripar = (v_notexateo * c_valexateo) + (v_notexapra * c_valesapra)
   v_notdefexapra = v_notexapra
   v_notdefexateo = v_notexateo 
   print()

   print(f"{v_nomest} su nota del primer parcial es: {v_notdefpripar:.2f}")
   print()

   # Calcula suma de las notas de todos los estudiantes 
   v_sumnotpripar = v_sumnotpripar + v_notdefpripar
   print(f"La sumatoria de todas las notas de los estudiantes es: {v_sumnotpripar:.2f}")
   print()

   # calcular promedio del parical por genero 

   if v_genEst == 1:
     acusumdeh = acusumdeh + v_notdefpripar
     acucantesth += 1
     v_pronotparh = acusumdeh / acucantesth
     

     if v_notdefpripar > v_notmaxh:
         v_notmaxh = v_notdefpripar
     elif v_notdefpripar < v_notminh:
         v_notminh = v_notdefpripar
      
   elif v_genEst == 2:
     acusumdem = acusumdem + v_notdefpripar
     acucantestm += 1
     v_pronotparm = acusumdem / acucantestm

     if  v_notdefpripar > v_notmaxm:
         v_notmaxm = v_notdefpripar
     elif v_notdefpripar < v_notminm:
         v_notminm = v_notdefpripar 
   else:
    equivocado = "Se equivoco de genero"

    # Calcular nota maxima y minima 
    print(f"La nota maxima del grupo femenino es: {v_notmaxm} y la nota minima es: {v_notminm}")
    print(f"La nota maxima del grupo masculino es: {v_notmaxh} y la nota minima es: {v_notminh}")
    print()


    # calcular promedio del grupo de las notas del primer parcial 
    
    print(f"El promedio del grupo de mujeres del primer parcial es: {v_pronotparm:.2f}")
    print(f"El promedio del grupo de hombres del primer parcial es: {v_pronotparh:.2f}")
    print()

v_pronotpripar = v_sumnotpripar / v_cantest
print(f"El promedio del grupo del primer parcial es: {v_pronotpripar:.2f}")

v_pronotpripra = v_notdefexapra / v_cantest
print(f"El promedio del grupo del primer parcial practico es: {v_pronotpripra:.2f}")

v_pronotpriteo = v_notdefexateo / v_cantest
print(f"El promedio del grupo del primer parcial teorico es: {v_pronotpriteo:.2f}")
print()





 



