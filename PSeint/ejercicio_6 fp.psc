Algoritmo ejercicio_6
	// Descripcion: progama que lee tres números A, B, C y visualiza en pantalla el valor del más grande. Se supone que los tres valores son diferentes //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 05/03/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir A,B,C,mayor Como Real
	// Inicializar variables //
	A <- 0
	B <- 0
	C <- 0
	// Entrada de datos //
	Escribir 'Escriba el numero A'
	Leer A
	Escribir 'Escriba el numero B'
	Leer B
	Escribir 'Escriba el numero C'
	Leer C
	// Procesos //
	Si A>B Entonces
		Si A>C Entonces
			Escribir 'El numero mayor es el A: ',A
		FinSi
	FinSi
	Si B>A Entonces
		Si B>C Entonces
			Escribir 'El numero mayor es el B: ',B
		FinSi
	FinSi
	Si C>B Entonces
		Si C>A Entonces
			Escribir 'El numero mayor es el C: ',C
		FinSi
	FinSi
FinAlgoritmo
