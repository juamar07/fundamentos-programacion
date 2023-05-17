Algoritmo problema_7
	// Descripcion: progrma calcula el producto de los n primeros números naturales //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 26/02/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir fact,n Como Real
	Definir i Como Entero
	// AREA DE CAPTURA DE DATOS //
	Escribir 'Digite un numero natural: '
	Leer n
	// AREA DE CALCULOS // 
	fact <- 1
	// AREA DE SALIDA //
	Si n>=0 Entonces
		Para i<-1 Hasta n Hacer
			fact <- (fact*i)
		FinPara
		Escribir 'el factorial es: ',fact
	SiNo
		Escribir 'no existe factorial'
	FinSi
FinAlgoritmo
