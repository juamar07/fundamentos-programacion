Algoritmo problema_9
	// Descripcion: programa recibe tres números enteros e imprime el mayor de ellos.  //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 26/02/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir a,b,c,d Como Entero
	// AREA DE CAPTURA DE DATOS //
	Escribir 'Digite el primer numero: '
	Leer a
	Escribir 'Digite el segundo numero: '
	Leer b
	Escribir 'Digite el tercer numero: '
	Leer c
	// AREA DE CALCULOS // 
	Si a>b Y b>c Entonces
		Escribir 'el numero mayor es el primero:',a
		Si b>a Y a>c Entonces
			Escribir 'el numero mayor es el segundo:',b
		SiNo
			Escribir 'el numero mayor es el tercero:',c
		FinSi
	FinSi
FinAlgoritmo
