Algoritmo ejercicio_4
	// Descripcion: progama que lee vel inicial, vel final y aceleraccion, y aplica la formula de tiempo // 
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 22/02/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir a,b,c,d Como Real
	// AREA DE CAPTURA DE DATOS //
	Escribir 'Digite la velocidad inicial en m/s: '
	Leer a
	Escribir 'Digite la velocidad final en m/s: '
	Leer b
	Escribir 'Digite la aceleracion en m/s**2: '
	Leer c
	// AREA DE CALCULOS //
	d <- (b-a)/(c)
	// AREA DE SALIDA //
	Escribir 'El tiempo es de: ',d,' segundos'
FinAlgoritmo
