Algoritmo parcial1_ejer2
	// Area de documentacion //
	// Descripcion: progama que pide al usuario los datos de un préstamo hipotecario (capital prestado, interés anual y años que dura el préstamo) y le muestre la cuota mensual que habrá de pagar y el total de lo pagado una vez terminado el plazo, distinguiendo la cantidad de amortización y la de intereses.// 
	// Desarrollado por: Juan Martin Betancur y Nicolas Barbosa //
	// Version 1.0 //
	// Fecha ultima actualizacion: 13/03/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir capital,interes_anual,interes_mensual,intereses,plazo_meses,plazo_anios,cuota,total_pagado,amortizacion Como Real
	// Entrada de datos //
	Escribir 'Ingrese el capital prestado: '
	Leer capital
	Escribir 'Ingrese el interés anual: '
	Leer interes_anual
	Escribir 'Ingrese el plazo en años: '
	Leer plazo_anios
	// Area de calculos //
	interes_mensual <- interes_anual/12
	plazo_meses <- plazo_anios*12
	ratio <- interes_mensual/100
	plazo_meses <- plazo_meses*(-1)
	cuota <- (capital*ratio)/(1-(1+ratio)^plazo_meses)
	total_pagado <- cuota*plazo_meses
	amortizacion <- capital
	intereses <- total_pagado-capital
	// Salida de datos //
	Escribir 'La cuota mensual es: ',cuota
	Escribir 'El total pagado es: ',total_pagado
	Escribir 'La cantidad de amortización es: ',amortizacion
	Escribir 'La cantidad de intereses es: ',intereses
FinAlgoritmo
