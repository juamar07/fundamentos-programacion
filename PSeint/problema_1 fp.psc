Algoritmo problema_1
	
	// Descripcion: progama que lee nombre del usuario, horas trabajadas, precio de la hora e impuestos a pagar y da como resultado el salario bruto y el salario neto.
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 25/02/2023 // 
	
	// AREA DEFINICION DE VARIABLES //
	
	Definir horat,preciot,impue,salariob,tasas,salarion Como Real
	
	// AREA DE CAPTURA DE DATOS //
	
	Escribir 'escriba su nombre: '
	Leer nom
	
	Escribir 'digite la cantidad de horas trabajadas: '
	Leer horat
	
	Escribir 'Digite el precio de la hora trabajada: '
	Leer preciot
	
	Escribir 'Digite el porcentaje del valor de los impuestos: '
	Leer impue
	
	// AREA DE CALCULOS // 
	
	salariob <- (horat*preciot)
	tasas <- (impue*salariob)
	salarion <- (salariob-tasas)
	
	// AREA DE SALIDA //
	
	Escribir nom,' Su salario neto es de: ',salarion,' pesos'
	
FinAlgoritmo
