   	# Area de documentacion //
	# Descripcion: progama que lee velocidad inicial, velocidad final, tiempo, aceleracion y distancia y aplica la formula para hallar cada una de las anteriores, segun elija el usuario // 
	# Desarrollado por: Juan Martin Betancur y Nicolas Barbosa //
	# Version 1.0 //
	# Fecha ultima actualizacion: 13/03/2023 // 
	# AREA DEFINICION DE VARIABLES //
print()
while True:
	opcio = int()
	velocidad_inicial = float()
	velocidad_media = float()
	velocidad_final = float()
	tiempo = float()
	aceleracion = float()
	distancia = float()
	tiempo1 = float()
	aceleraccionmed = float()
	print("Este programa sirve para calcular variables del movimiento rectilineo uniforme, los datos que vaya a ingresar tienen que estar en m/s")
	# Entrada de datos //
	print("Seleccione una opcion del menu: ")
	print("1. Calcular Velocidad media")
	print("2. Calcular Velocidad final")
	print("3. calcular velocidad final con variable al cuadrado")
	print("4. Calcular Aceleraccion")
	print("5. calcular aceleraccion media")
	print("6. Calcular Distancia con tiempo")
	print("7. calcular Distancia con tiempo y acelerccion")
	print("8. salir")
	print("Digite la opcion del menu que desea seleccionar")
	opcio = int(input())
	# Procesos //
	if opcio==1:
		print("Ingrese la velocidad inicial en m/s: ")
		velocidad_inicial = float(input())
		print("Ingrese la velocidad final en m/s: ")
		velocidad_final = float(input())
		print("Ingrese el tiempo en s: ")
		tiempo = float(input())
		velocidad_media = (velocidad_inicial+velocidad_final)/2
		print("La velocidad media es: ",velocidad_media," m/s")
	if opcio==2:
		print("Ingrese la velocidad inicial en m/s: ")
		velocidad_inicial = float(input())
		print("Ingrese la aceleracion en m/s^2: ")
		aceleracion = float(input())
		print("Ingrese el tiempo en s: ")
		tiempo = float(input())
		velocidad_final = velocidad_inicial+aceleracion*tiempo
		print("La velocidad final es: ",velocidad_final," m/s")
	if opcio==3:
		print("ingrese velocidad inicial al cuadrado en m/s: ")
		velocidad_inicial_al_cuadrado = float(input())
		print("ingrese distancia en m: ")
		distancia = float(input())
		print("ingrese aceleracion en m/s: ")
		aceleracion = float(input())
		velocidad_final_al_cuadrado = velocidad_inicial_al_cuadrado**2+2*aceleracion*distancia
		print("la velocidad final al cuadrado es: ",velocidad_final_al_cuadrado," m/s")
	if opcio==4:
		print("Ingrese la velocidad inicial en m/s: ")
		velocidad_inicial = float(input())
		print("Ingrese la velocidad final en m/s: ")
		velocidad_final = float(input())
		print("Ingrese el tiempo en s: ")
		tiempo = float(input())
		aceleracion = (velocidad_final-velocidad_inicial)/tiempo
		print("La aceleracion es: ",aceleracion," m/s^2")
	if opcio==6:
		print("Ingrese la velocidad inicial en m/s: ")
		velocidad_inicial = float(input())
		print("Ingrese la aceleracion en m/s^2: ")
		aceleracion = float(input())
		print("Ingrese el tiempo en s: ")
		tiempo = float(input())
		distancia = velocidad_inicial*tiempo+(1/2)*aceleracion*tiempo**2
		print("La distancia recorrida es: ",distancia," m")
	if opcio==7:
		print("Ingrese la aceleracion en m/s^2: ")
		aceleracion = float(input())
		print("Ingrese el tiempo en s: ")
		tiempo = float(input())
		print("Ingrese la velocidad inicial en m/s: ")
		velocidad_inicial = float(input())
		distancia = (velocidad_inicial*tiempo)+(1/2)*(aceleracion*(tiempo**2))
		print("La distancia recorrida es: ",distancia," m")
	if opcio==5:
		print("Ingrese la velocidad inicial en m/s: ")
		velocidad_inicial = float(input())
		print("Ingrese la velocidad final en m/s: ")
		velocidad_final = float(input())
		print("Ingrese el tiempo inicial en s: ")
		tiempo = float(input())
		print("Ingrese el tiempo fianl en s: ")
		tiempo1 = float(input())
		aceleracion = (velocidad_final-velocidad_inicial)/(tiempo1-tiempo)
		print("La aceleracion media es: ",aceleracion," m/s^2")
	if opcio<1:
		print("Opcion incorrecta vuelva al menu")
	if opcio>7:
		print("Opcion incorrecta vuelva al menu")
	elif opcio ==8:
		break

