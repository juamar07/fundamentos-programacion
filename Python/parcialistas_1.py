#Parcial 2 
#descripcion: Programa que calcula los resulatdos de los equipos de la liga colombiana
#fecha:  4/05/23
#desarrollado por: Juan Martin Betancur Uribe, Juan Sebastian Rodriguez Castaño, Mateo Arias Valencia
#version: 1.0

while True: 

    # Importar librerias para las graficas

    import matplotlib.pyplot as plt
    print()

    #calcular la cantidad de partidos ganados por equipo 

    partidos = [("once caldas", (3, 1), "millonarios "),
                ("nacional", (2, 2), "Envigado"),  
                ("once caldas ", (2, 0), "nacional"),
                ("millonarios", (1, 1), "Envigado"),
                ("once caldas", (1, 0), "envigado"),
                ("millonarios", (2, 1), "nacional"),
                ("santa fe",(3,1), "pasto"),
                ("jaguares",(1,1),"america de cali"),
                ("pasto",(3,2),"jaguares"),
                ("america de cali",(4,4),"santa fe"),]

    # Menu de opciones 

    print("si desea saber la cantidad de partidos por equipo presione 1")
    print("si desea saber la cantidad de partidos ganados por equipo presione 2")
    print("si desea saber la cantidad de partidos perdidos por equipos presione 3")
    print("si desea saber la cantidad de partidos empatados por equipo presione 4")
    print("si desea saber la cantidad de goles de los equipos locales y visitantes, presione 5")
    print("si desea saber cual es la cantidad de goles de todos los partidos, presione 6")
    print("si desea saber la cantidad de partidos por equipo presione 7")
    print("si desea saber cual es el equipo que mas goles realizo presione 8")
    print("si desea saber cual es el equipo que menos goles recibio presione 9")
    print("si desea ver un listado de los equipos con sus goles de local y visitante presione 10")
    print("si desea ver una tabla de posiciones presione 11")
    print("Si desea salir del programa, presione 0")

    opcionm = int(input("Seleccione una opcion del menu: "))
    print()

    if opcionm == 1:

        # Inicializar un diccionario vacío para almacenar la cantidad de partidos ganados por cada equipo

        partidos_ganados_por_equipo = {}

        partidos_por_equipo = {}
        for partido in partidos:
            equipo_local = partido[0]
            equipo_visitante = partido[2]
            if equipo_local not in partidos_por_equipo:
                partidos_por_equipo[equipo_local] = 1
            else:
                partidos_por_equipo[equipo_local] += 1
            if equipo_visitante not in partidos_por_equipo:
                partidos_por_equipo[equipo_visitante] = 1
            else:
                partidos_por_equipo[equipo_visitante] += 1

        print(partidos_por_equipo)

    if opcionm == 2:

    # Recorrer todos los partidos y calcular los partidos ganados por cada equipo

        partidos_ganados_por_equipo = {}
        for partido in partidos:
            equipo_local = partido[0]
            goles_local = partido[1][0]
            equipo_visitante = partido[2]
            goles_visitante = partido[1][1]
            
            # Comparar los goles de cada equipo para determinar el ganador

            if goles_local > goles_visitante:
                equipo_ganador = equipo_local
            elif goles_local < goles_visitante:
                equipo_ganador = equipo_visitante
            else:
                continue
            
            # Incrementar el contador de partidos ganados del equipo correspondiente en el diccionario

            if equipo_ganador in partidos_ganados_por_equipo:
                partidos_ganados_por_equipo[equipo_ganador] += 1
            else:
                partidos_ganados_por_equipo[equipo_ganador] = 1

        # Imprimir la cantidad de partidos ganados por cada equipo

        for equipo, partidos_ganados in partidos_ganados_por_equipo.items():
            print("{} ganó {} partidos".format(equipo, partidos_ganados))

    if opcionm == 3:

        # calcular la cantidad de partidos perdidos por equipo 

        partidos = [("once caldas", (3, 1), "millonarios "),
                    ("nacional", (2, 2), "Envigado"),  
                    ("once caldas ", (2, 0), "nacional"),
                    ("millonarios", (1, 1), "Envigado"),
                    ("once caldas", (1, 0), "envigado"),
                    ("millonarios", (2, 1), "nacional"),
                    ("santa fe",(3,1), "pasto"),
                    ("jaguares",(1,1),"america de cali"),
                    ("pasto",(3,2),"jaguares"),
                    ("america de cali",(4,4),"santa fe"),]

        # Inicializar un diccionario vacío para almacenar la cantidad de partidos perdidos por cada equipo

        partidos_perdidos_por_equipo = {}

        # Recorrer todos los partidos y calcular los partidos perdidos por cada equipo

        for partido in partidos:
            equipo_local = partido[0]
            goles_local = partido[1][0]
            equipo_visitante = partido[2]
            goles_visitante = partido[1][1]
            
            # Comparar los goles de cada equipo para determinar el perdedor

            if goles_local < goles_visitante:
                equipo_perdedor = equipo_local
            elif goles_local > goles_visitante:
                equipo_perdedor = equipo_visitante
            else:
                continue
            
            # Incrementar el contador de partidos perdidos del equipo correspondiente en el diccionario

            if equipo_perdedor in partidos_perdidos_por_equipo:
                partidos_perdidos_por_equipo[equipo_perdedor] += 1
            else:
                partidos_perdidos_por_equipo[equipo_perdedor] = 1

        # Imprimir la cantidad de partidos perdidos por cada equipo

        for equipo, partidos_perdidos in partidos_perdidos_por_equipo.items():
            print("{} perdió {} partidos".format(equipo, partidos_perdidos))

    if opcionm == 4:

        #calcular la cantidad de partidos empatados por equipo

        partidos = [("once caldas", (3, 1), "millonarios "),
                    ("nacional", (2, 2), "Envigado"),  
                    ("once caldas ", (2, 0), "nacional"),
                    ("millonarios", (1, 1), "Envigado"),
                    ("once caldas", (1, 0), "envigado"),
                    ("millonarios", (2, 1), "nacional"),
                    ("santa fe",(3,1), "pasto"),
                    ("jaguares",(1,1),"america de cali"),
                    ("pasto",(3,2),"jaguares"),
                    ("america de cali",(4,4),"santa fe"),] 

        # Inicializar un diccionario vacío para almacenar la cantidad de partidos empatados por cada equipo

        partidos_empatados_por_equipo = {}

        # Recorrer todos los partidos y calcular los partidos empatados por cada equipo

        for partido in partidos:
            equipo_local = partido[0]
            goles_local = partido[1][0]
            equipo_visitante = partido[2]
            goles_visitante = partido[1][1]
            
            # Comparar los goles de cada equipo para determinar si el partido fue un empate

            if goles_local == goles_visitante:
                equipos_empatados = (equipo_local, equipo_visitante)
                
                # Incrementar el contador de partidos empatados de cada equipo en el diccionario

                for equipo in equipos_empatados:
                    if equipo in partidos_empatados_por_equipo:
                        partidos_empatados_por_equipo[equipo] += 1
                    else:
                        partidos_empatados_por_equipo[equipo] = 1

        # Imprimir la cantidad de partidos empatados por cada equipo

        for equipo, partidos_empatados in partidos_empatados_por_equipo.items():
            print("{} empató {} partidos".format(equipo, partidos_empatados))


    if opcionm == 7:

    #calcular la cantidad de goles de todos los partidos

        partidos = [('once caldas', 2, 'millonarios', 1),           
                    ('nacional', 0, 'envigado', 0),           
                    ('once caldas', 1, 'nacional', 1),           
                    ('millonarios', 2, 'envigado', 2),
                    ('santa fe', 1, 'pasto', 2),
                    ('jaguares', 3, 'america de cali', 4),
                    ('america de cali', 2, 'santa fe', 2),
                    ('pasto', 3, 'jaguares', 0)]
                    


        total_goles = 0

        for partido in partidos:
            goles_local = partido[1]
            goles_visitante = partido[3]
            total_goles += goles_local + goles_visitante

        print("La cantidad total de goles en todos los partidos es:", total_goles)

    if opcionm == 6:

        #calcular la cantidad de partidos por  equipo

        partidos = [('once caldas', 'millonarios'),          
                    ('nacional', 'envigado'),           
                    ('once caldas', 'nacional'),          
                    ('millonarios', 'envigado'),         
                    ('once caldas', 'envigado'),
                    ('santa fe', 'pasto'),
                    ('jaguares', 'america de cali'),
                    ('america de cali', 'santa fe'),
                    ('pasto', 'jaguares')]

        partidos_por_equipo = {}

        for partido in partidos:
            equipo_local = partido[0]
            equipo_visitante = partido[1]
            
            if equipo_local in partidos_por_equipo:
                partidos_por_equipo[equipo_local] += 1
            else:
                partidos_por_equipo[equipo_local] = 1
            
            if equipo_visitante in partidos_por_equipo:
                partidos_por_equipo[equipo_visitante] += 1
            else:
                partidos_por_equipo[equipo_visitante] = 1

        print("La cantidad de partidos por equipo es:", partidos_por_equipo)

    if opcionm == 5:

        #lista de los equipos con su total de goles de local y visitante

        partidos = [('once caldas', 2, 'millonarios', 1),           
                    ('nacional', 0, 'envigado', 0),           
                    ('once caldas', 1, 'nacional', 1),           
                    ('millonarios', 2, 'envigado', 2),           
                    ('once caldas', 3, 'envigado', 1),
                    ('santa fe', 1, 'pasto', 2),
                    ('jaguares', 3, 'america de cali', 4),
                    ('america de cali', 2, 'santa fe', 2),
                    ('pasto', 3, 'jaguares', 0)]

        goles_por_equipo = {}

        for partido in partidos:
            equipo_local = partido[0]
            goles_local = partido[1]
            equipo_visitante = partido[2]
            goles_visitante = partido[3]

            if equipo_local in goles_por_equipo:
                goles_por_equipo[equipo_local][0] += goles_local
                goles_por_equipo[equipo_local][1] += goles_visitante
            else:
                goles_por_equipo[equipo_local] = [goles_local, goles_visitante]

            if equipo_visitante in goles_por_equipo:
                goles_por_equipo[equipo_visitante][0] += goles_visitante
                goles_por_equipo[equipo_visitante][1] += goles_local
            else:
                goles_por_equipo[equipo_visitante] = [goles_visitante, goles_local]

        lista_goles_por_equipo = []

        for equipo, goles in goles_por_equipo.items():
            lista_goles_por_equipo.append((equipo, goles[0], goles[1]))

        nombres = [equipo[0] for equipo in lista_goles_por_equipo]
        goles_local = [equipo[1] for equipo in lista_goles_por_equipo]
        goles_visitante = [equipo[2] for equipo in lista_goles_por_equipo]

        plt.figure(figsize=(10,8))
        plt.barh(nombres, goles_local, label='Goles de local', color='blue')
        plt.barh(nombres, goles_visitante, label='Goles de visitante', color='red', left=goles_local)
        plt.xlabel('Goles')
        plt.ylabel('Equipos')
        plt.title('Total de goles de local y visitante por equipo')
        plt.legend()
        plt.show()

        print("La lista de equipos con su total de goles de local y visitante es:", lista_goles_por_equipo)

    if opcionm == 8:

        #calcular que equipo realizo mas goles

        partidos = [('once caldas', 2, 'millonarios', 1),           
                    ('nacional', 0, 'envigado', 0),           
                    ('once caldas', 1, 'nacional', 1),           
                    ('millonarios', 2, 'envigado', 2),           
                    ('once caldas', 3, 'envigado', 1),
                    ('santa fe', 1, 'pasto', 2),
                    ('jaguares', 3, 'america de cali', 4),
                    ('america de cali', 2, 'santa fe', 2),
                    ('pasto', 3, 'jaguares', 0)]

        goles_por_equipo = {}

        for partido in partidos:
            equipo_local = partido[0]
            goles_local = partido[1]
            equipo_visitante = partido[2]
            goles_visitante = partido[3]

            if equipo_local in goles_por_equipo:
                goles_por_equipo[equipo_local] += goles_local
            else:
                goles_por_equipo[equipo_local] = goles_local

            if equipo_visitante in goles_por_equipo:
                goles_por_equipo[equipo_visitante] += goles_visitante
            else:
                goles_por_equipo[equipo_visitante] = goles_visitante

        max_goles = max(goles_por_equipo.values())
        equipos_max_goles = [equipo for equipo, goles in goles_por_equipo.items() if goles == max_goles]

        print("El equipo(s) que realizo ma0s goles es:", equipos_max_goles)

    if opcionm == 9:

        #equipo que menos goles recibio 

        partidos = [('once caldas', 2, 'millonarios', 1),           
                    ('nacional', 0, 'envigado', 0),           
                    ('once caldas', 1, 'nacional', 1),           
                    ('millonarios', 2, 'envigado', 2),           
                    ('once caldas', 3, 'envigado', 1),
                    ('santa fe', 1, 'pasto', 2),
                    ('jaguares', 3, 'america de cali', 4),
                    ('america de cali', 2, 'santa fe', 2),
                    ('pasto', 3, 'jaguares', 0)]

        goles_recibidos_por_equipo = {}

        for partido in partidos:
            equipo_local = partido[0]
            goles_local = partido[1]
            equipo_visitante = partido[2]
            goles_visitante = partido[3]

            if equipo_local in goles_recibidos_por_equipo:
                goles_recibidos_por_equipo[equipo_local] += goles_visitante
            else:
                goles_recibidos_por_equipo[equipo_local] = goles_visitante

            if equipo_visitante in goles_recibidos_por_equipo:
                goles_recibidos_por_equipo[equipo_visitante] += goles_local
            else:
                goles_recibidos_por_equipo[equipo_visitante] = goles_local

        equipos_menos_goles_recibidos = sorted(goles_recibidos_por_equipo.items(), key=lambda x: x[1])[0][0]

        print("El equipo que menos goles recibió en el torneo es:", equipos_menos_goles_recibidos)

    if opcionm == 10:

        # Definir lista de tuplas con los equipos y su puntaje

        equipos =  []
        equipos = [("once caldas", 10), ("millonarios", 8), ("nacional", 12), ("envigado", 6), ("santa fe", 5), ("pasto", 7), ("jaguares", 8), ("america de cali", 10)]
        print(equipos)

    # Ordenar equipos por puntaje (de mayor a menor)

    if opcionm == 11:
        equipos_ordenados = sorted(equipos, key=lambda x: x[1], reverse=True)

        # Imprimir tabla de posiciones

        print("Tabla de posiciones:")
        print("Posición\tEquipo\t\tPuntaje")
        
        for i, equipo in enumerate(equipos_ordenados):
            print(f"{i+1}\t\t{equipo[0]}\t{equipo[1]}")

    if opcionm > 11:
        print("Se equivoco de ocpcion del menu, vuelva a intentarlo")
    
    if opcionm == 0:
        print("Gracias por usar este programa")
        print()
        break
