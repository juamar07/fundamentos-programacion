Algoritmo ejer_deciciones_2
	// Descripcion: progama que lee dos numeros e impreme cual es el mayor //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 27/02/2023 // 
	
	// AREA DEFINICION DE VARIABLES //
	
	Definir  num1, num2, nummay Como Entero
	
	// Inicializar variables //
	
	num1<-0
	num2<-0
	nummay<-0
	
	// Entrada de datos //
	
	Escribir 'digite un numero'
	leer num1
	
	Escribir 'digite otro numero'
	leer num2
	
	Si num1=num2 Entonces
		Escribir 'los dos numeros son iguales'
	SiNo
		Si num1>num2 Entonces
			nummay=num1
		SiNo
			nummay=num2
		Fin Si
		
		Escribir 'el numero mayor es: ',nummay
		
	Fin Si
	
	
	
FinAlgoritmo
