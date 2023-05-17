Algoritmo parcial_1
	// Area de documentacion //
	// Descripcion: progama que lee velocidad inicial, velocidad final, tiempo, aceleracion y distancia y aplica la formula para hallar cada una de las anteriores, segun elija el usuario // 
	// Desarrollado por: Juan Martin Betancur y Nicolas Barbosa //
	// Version 1.0 //
	// Fecha ultima actualizacion: 13/03/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir opcio Como Entero
	Definir velocidad_inicial,velocidad_media,velocidad_final,tiempo,aceleracion,distancia,tiempo1,aceleraccionmed Como Real
	Escribir 'Este programa sirve para calcular variables del movimiento rectilineo uniforme, los datos que vaya a ingresar tienen que estar en m/s'
	// Entrada de datos //
	Escribir 'Seleccione una opcion del menu: '
	Escribir '1. Calcular Velocidad media'
	Escribir '2. Calcular Velocidad final'
	Escribir '3. calcular velocidad final con variable al cuadrado'
	Escribir '4. Calcular Aceleraccion'
	Escribir '5. calcular aceleraccion media'
	Escribir '6. Calcular Distancia con tiempo'
	Escribir '7. calcular Distancia con tiempo y acelerccion'
	Escribir 'Digite la opcion del menu que desea seleccionar'
	Leer opcio
	// Procesos //
	Si opcio=1 Entonces
		Escribir 'Ingrese la velocidad inicial en m/s: '
		Leer velocidad_inicial
		Escribir 'Ingrese la velocidad final en m/s: '
		Leer velocidad_final
		Escribir 'Ingrese el tiempo en s: '
		Leer tiempo
		velocidad_media <- (velocidad_inicial+velocidad_final)/2
		Escribir 'La velocidad media es: ',velocidad_media,' m/s'
	FinSi
	Si opcio=2 Entonces
		Escribir 'Ingrese la velocidad inicial en m/s: '
		Leer velocidad_inicial
		Escribir 'Ingrese la aceleración en m/s^2: '
		Leer aceleracion
		Escribir 'Ingrese el tiempo en s: '
		Leer tiempo
		velocidad_final <- velocidad_inicial+aceleracion*tiempo
		Escribir 'La velocidad final es: ',velocidad_final,' m/s'
	FinSi
	Si opcio=3 Entonces
		Escribir 'ingrese velocidad inicial al cuadrado en m/s: '
		Leer velocidad_inicial_al_cuadrado
		Escribir 'ingrese distancia en m: '
		Leer distancia
		Escribir 'ingrese aceleracion en m/s: '
		Leer aceleracion
		velocidad_final_al_cuadrado <- velocidad_inicial_al_cuadrado^2+2*aceleracion*distancia
		Escribir 'la velocidad final al cuadrado es: ',velocidad_final_al_cuadrado,' m/s'
	FinSi
	Si opcio=4 Entonces
		Escribir 'Ingrese la velocidad inicial en m/s: '
		Leer velocidad_inicial
		Escribir 'Ingrese la velocidad final en m/s: '
		Leer velocidad_final
		Escribir 'Ingrese el tiempo en s: '
		Leer tiempo
		aceleracion <- (velocidad_final-velocidad_inicial)/tiempo
		Escribir 'La aceleración es: ',aceleracion,' m/s^2'
	FinSi
	Si opcio=6 Entonces
		Escribir 'Ingrese la velocidad inicial en m/s: '
		Leer velocidad_inicial
		Escribir 'Ingrese la aceleración en m/s^2: '
		Leer aceleracion
		Escribir 'Ingrese el tiempo en s: '
		Leer tiempo
		distancia <- velocidad_inicial*tiempo+(1/2)*aceleracion*tiempo^2
		Escribir 'La distancia recorrida es: ',distancia,' m'
	FinSi
	Si opcio=7 Entonces
		Escribir 'Ingrese la aceleración en m/s^2: '
		Leer aceleracion
		Escribir 'Ingrese el tiempo en s: '
		Leer tiempo
		Escribir 'Ingrese la velocidad inicial en m/s: '
		Leer velocidad_inicial
		distancia <- (velocidad_inicial*tiempo)+(1/2)*(aceleracion*(tiempo^2))
		Escribir 'La distancia recorrida es: ',distancia,' m'
	FinSi
	Si opcio=5 Entonces
		Escribir 'Ingrese la velocidad inicial en m/s: '
		Leer velocidad_inicial
		Escribir 'Ingrese la velocidad final en m/s: '
		Leer velocidad_final
		Escribir 'Ingrese el tiempo inicial en s: '
		Leer tiempo
		Escribir 'Ingrese el tiempo fianl en s: '
		Leer tiempo1
		aceleracion <- (velocidad_final-velocidad_inicial)/(tiempo1-tiempo)
		Escribir 'La aceleración media es: ',aceleracion,' m/s^2'
	FinSi
	Si opcio<1 Entonces
		Escribir 'Opcion incorrecta vuelva al menu'
	FinSi
	Si opcio>7 Entonces
		Escribir 'Opcion incorrecta vuelva al menu'
	FinSi
FinAlgoritmo
