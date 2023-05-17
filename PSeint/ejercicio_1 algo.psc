Algoritmo ejercicio_1
	// Descripcion: progama que lee vel inicial, vel final y tiempo, y aplica la formula de aceleracion // 
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 22/02/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir a,b,c,d Como Entero
	// AREA DE CAPTURA DE DATOS //
	Escribir 'Digite la velocidad inicial en m/s'
	Leer a
	Escribir 'Digite la velocidad final en m/s'
	Leer b
	Escribir 'Digite el tiempo en s'
	Leer c
	// AREA DE CALCULOS //
	d <- (b-a)/(c)
	// AREA DE SALIDA //
	Escribir 'la aceleracion es de: ',d,' m/s**2'
FinAlgoritmo
