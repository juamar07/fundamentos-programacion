# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de documentacion //
	# Descripcion: progama que pide al usuario los datos de un pr�stamo hipotecario (capital prestado, inter�s anual y a�os que dura el pr�stamo) y le muestre la cuota mensual que habr� de pagar y el total de lo pagado una vez terminado el plazo, distinguiendo la cantidad de amortizaci�n y la de intereses.// 
	# Desarrollado por: Juan Martin Betancur y Nicolas Barbosa //
	# Version 1.0 //
	# Fecha ultima actualizacion: 13/03/2023 // 
	# AREA DEFINICION DE VARIABLES //
	capital = float()
	interes_anual = float()
	interes_mensual = float()
	intereses = float()
	plazo_meses = float()
	plazo_anios = float()
	cuota = float()
	total_pagado = float()
	amortizacion = float()
	# Entrada de datos //
	print("Ingrese el capital prestado: ")
	capital = float(input())
	print("Ingrese el interes anual: ")
	interes_anual = float(input())
	print("Ingrese el plazo en anos: ")
	plazo_anios = float(input())
	# Area de calculos //
	interes_mensual = interes_anual/12
	plazo_meses = plazo_anios*12
	ratio = interes_mensual/100
	plazo_meses = plazo_meses*(-1)
	cuota = (capital*ratio)/(1-(1+ratio)**plazo_meses)
	total_pagado = cuota*plazo_meses
	amortizacion = capital
	intereses = total_pagado-capital
	# Salida de datos //
	print("La cuota mensual es: ",cuota)
	print("El total pagado es: ",total_pagado)
	print("La cantidad de amortizacion es: ",amortizacion)
	print("La cantidad de intereses es: ",intereses)

