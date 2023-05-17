# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: progama que lee dos numeros e impreme cual es el mayor //
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 27/02/2023 // 
	# AREA DEFINICION DE VARIABLES //
	num1 = int()
	num2 = int()
	nummay = int()
	# Inicializar variables //
	num1 = 0
	num2 = 0
	nummay = 0
	# Entrada de datos //
	print("digite un numero")
	num1 = int(input())
	print("digite otro numero")
	num2 = int(input())
	if num1==num2:
		print("los dos numeros son iguales")
	else:
		if num1>num2:
			nummay = num1
		else:
			nummay = num2
		print("el numero mayor es: ",nummay)

