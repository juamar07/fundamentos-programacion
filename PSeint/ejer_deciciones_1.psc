Algoritmo ejer_deciciones_1
	// Descripcion: progama que lee dos numeros e impreme cual es el mayor //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 27/02/2023 // 
	
	// AREA DEFINICION DE VARIABLES //
	
	Definir  num1, num2 Como Entero
	
	// Inicializar variables //
	
	num1<-0
	num2<-0
	
	// Entrada de datos //
	
	Escribir 'digite un numero'
	leer num1
	
	Escribir 'digite otro numero'
	leer num2
	
	// Procesos //
	
	Si num1>num2 Entonces
		Escribir 'El numero uno es el mayor: ',num1
	Fin Si
		
	si num1=num2 Entonces
		Escribir 'los dos numeros son iguales: ',num1
	Fin Si
	
	si num1<num2 Entonces
		Escribir 'El numero dos es el mayor: ',num2 
	Fin Si
	
	
FinAlgoritmo
