Algoritmo problema_5
	// Descripcion: progrma que calcula el valor de una llamada teniendo en cuenta los minutos extras //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 26/02/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir min,mine,precio Como Real
	// AREA DE CAPTURA DE DATOS //
	Escribir 'digite la cantidad de minutos hablados:'
	Leer min
	mine <- 3
	Si min<=3 Entonces
		precio <- 10
	SiNo
		precio <- ((min-3)*5)+10
	FinSi
	Escribir 'El valor de su llamada es de: ',precio,' centimos'
FinAlgoritmo
