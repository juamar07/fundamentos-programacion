# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: progrma que calcula el valor de una llamada teniendo en cuenta los minutos extras //
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 26/02/2023 // 
	# AREA DEFINICION DE VARIABLES //
	min = float()
	mine = float()
	precio = float()
	# AREA DE CAPTURA DE DATOS //
	print("digite la cantidad de minutos hablados:")
	min = float(input())
	mine = 3
	if min<=3:
		precio = 10
	else:
		precio = ((min-3)*5)+10
	print("El valor de su llamada es de: ",precio," centimos")

