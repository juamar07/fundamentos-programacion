Algoritmo ejercicio_2
	
	// Descripcion: progama que lee vel inicial, vel final y tiempo, y aplica la formula de aceleracion // 
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 22/02/2023 // 
	// AREA DEFINICION DE VARIABLES //
	
	definir a,b,c,d Como Real
	
	// AREA DE CAPTURA DE DATOS //
	
	Escribir 'Digite la velocidad inicial en km/h: '
	Leer a 
	
	Escribir 'Digite la velocidad final en km/h: '
	Leer b 
	
	Escribir 'Digite el tiempo en horas: '
	Leer c
	
	// AREA DE CALCULOS //
	
	d <- (b-a) / (c)
	
	// AREA DE SALIDA //
	
	
	Escribir 'la aceleracion es de: ',d
	
	
FinAlgoritmo
