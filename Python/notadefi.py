# Calculo de nota definitiva

while True:
    print()
    print("Este programa es para calcular notas definitivas")

    print()

    nom = input("Ingrese el nombre del estudiante: ")
    not1= float(input("Ingrese la nota del primer parcial: "))
    not2= float(input("Ingrese la nota del segundo parcial: "))
    not3= float(input("Ingrese la nota del tercer parcial: "))
    print()
    por1= int(input("Digite el porcentaje del valor del primer parcial: "))
    por2= int(input("Digite el porcentaje del valor del segundo parcial: "))
    por3= int(input("Digite el porcentaje del valor del tercer parcial: "))
    print()
    ina = int(input("Digite la cantidad de inasistencia: "))

    sump= por1 + por2 + por3

    nod1= not1 * (por1/100)
    nod2= not2 * (por2/100)
    nod3= not3 * (por3/100)
    print()
    if ina >= 12:
        print("Ha perdido la materia por inacistencia")
        if sump > 100:
            print("Ha ingrsado una cantidad de porcentajes mayor al 100%")
        elif sump >=99 or sump <=100:
            if not1 >5 or not2>5 or not3>5:
                print("Error, ha ingresado notas mayores a 5.0, vuelva a digitar las notas")
            elif not1 <=5 and not2<=5 and not3<=5:
               print(f"{nom}, Su nota definitiva es {(nod1+nod2+nod3)/2:.1f}")
        print()

    elif ina < 12:
        print("No pierde la materia por inacistencias")
        if sump > 100:
            print("Ha ingrsado una cantidad de porcentajes mayor al 100%")
        elif sump >=99 or sump <=100:
            if not1 >5 or not2>5 or not3>5:
                print("Error, ha ingresado notas mayores a 5.0, vuelva a digitar las notas")
            elif not1 <=5 and not2<=5 and not3<=5:
               print(f"{nom}, Su nota definitiva es {nod1+nod2+nod3:.1f}")
               conti= input("desea continuar en el programa: ")
               print()
               
               if conti == "si":
                   print("Ok, continuando con el programa")
                   print()

               else:
                   print("Gracias por usar este programa")
                   print()

                   break 