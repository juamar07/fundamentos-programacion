# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: progrma que suma todos los numeros enteros del uno al cincuenta.
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 26/02/2023 // 
	# AREA DEFINICION DE VARIABLES //
	suma = int()
	num = int()
	sum = 0
	num = 1
	# AREA DE CALCULOS // 
	while (num<=50):
		sum = (sum+num)
		num = (num+1)
	# AREA DE SALIDA //
	print("suma de numeros enteros entre el 1 y el 50 = ",sum)

