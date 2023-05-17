Algoritmo problema_6
	
	// Descripcion: progrma que suma todos los numeros enteros del uno al cincuenta.
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 26/02/2023 // 
	
	// AREA DEFINICION DE VARIABLES //
	
	Definir suma,num Como Entero
	sum <- 0
	num <- 1
	
	// AREA DE CALCULOS // 
	
	Mientras (num<=50) Hacer
		sum <- (sum+num)
		num <- (num+1)
	FinMientras
	
	// AREA DE SALIDA //
	
	Escribir 'suma de numeros enteros entre el 1 y el 50 = ',sum
	
FinAlgoritmo
