Algoritmo problema_2
	// Descripcion: progama que lee una cantidad de numeros, pide por teclado cada numero y calcula su promedio//
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 27/02/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir cannum,concic,num,sumnum Como Entero
	Definir prom Como Real
	// inicializacion de variables //
	cannum <- 0
	num <- 0
	sumnum <- 0
	prom <- 0.0
	// Entrada de de datos //
	Escribir 'Digite cantidad de numeros a promediar'
	Leer cannum
	Para concic<-1 Hasta cannum Hacer
		Escribir 'Digite un numero: '
		Leer num
		sumnum <- sumnum+num
	FinPara
	// Area de salida //
	prom <- sumnum/cannum
	Escribir 'El pormedio de los numeros es: ',prom
FinAlgoritmo
