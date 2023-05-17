# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: progrma calcula el producto de los n primeros números naturales //
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 26/02/2023 // 
	# AREA DEFINICION DE VARIABLES //
	fact = float()
	n = float()
	i = int()
	# AREA DE CAPTURA DE DATOS //
	print("Digite un numero natural: ")
	n = float(input())
	# AREA DE CALCULOS // 
	fact = 1
	# AREA DE SALIDA //
	if n>=0:
		for i in range(1,n+1):
			fact = (fact*i)
		print("el factorial es: ",fact)
	else:
		print("no existe factorial")

