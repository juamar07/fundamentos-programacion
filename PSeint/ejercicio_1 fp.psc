Algoritmo ejercicio_1
	// Descripcion: progama que soluciona funciones de primer grado //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 02/03/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir a,b,x Como Real
	// Entrada de datos //
	Escribir 'digite el numero correspondiente para a'
	Leer a
	Escribir 'digite el numero correspondiente para b'
	Leer b
	// Procesos //
	Si a<>0 Entonces
		x <- -b/a
		Escribir 'La solucion es: ',x
	SiNo
		Si b<>0 Entonces
			Escribir ('solución imposible')
		FinSi
	FinSi
FinAlgoritmo
