import random

nombres = ["Juan", "Martin", "Mateo", "Sebastian", "Valentina"]

for x in range(3):

    nombre_aleatorio = random.choice(nombres)
    edad = random.randint(16,20)
    notfin = random.randint(1,5)
    inasis = random.randint(1,15)
    print()

    if notfin < 3.0:
        print(f"{nombre_aleatorio} Pierde la materia por nota, la cual es {notfin}")
    else:
        print(f"{nombre_aleatorio} Gana la materia por notas, la cual es {notfin}")
        print()

    if inasis > 12:
        print(f"{nombre_aleatorio} Pierde la materia por inasistencias, las cuales fueron {inasis}")
    else: 
        print(f" {nombre_aleatorio} No pierde por inasistencias, las cuales fueron {inasis}")
        print()
        
    if notfin < 3.0 and inasis > 12:
        print(f"{nombre_aleatorio} Cambiese de carrera")
    else:
        print(f"{nombre_aleatorio} Esta en la carrera correcta")
        print()


