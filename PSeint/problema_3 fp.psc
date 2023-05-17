Algoritmo problema_3
	// Descripcion: progama que cuenta que cuenta todos los numeros pares entre el 2 y el 100 //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 25/02/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir suma,num Como Entero
	sum <- 2
	num <- 4
	// AREA DE CALCULOS // 
	Mientras (num<=100) Hacer
		sum <- (sum+num)
		num <- (num+2)
	FinMientras
	// AREA DE SALIDA //
	Escribir 'suma de numeros pares entre 2 y 100 = ',sum
FinAlgoritmo
