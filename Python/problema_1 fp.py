# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: progama que lee nombre del usuario, horas trabajadas, precio de la hora e impuestos a pagar y da como resultado el salario bruto y el salario neto.
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 25/02/2023 // 
	# AREA DEFINICION DE VARIABLES //
	horat = float()
	preciot = float()
	impue = float()
	salariob = float()
	tasas = float()
	salarion = float()
	# AREA DE CAPTURA DE DATOS //
	print("escriba su nombre: ")
	nom = input()
	print("digite la cantidad de horas trabajadas: ")
	horat = float(input())
	print("Digite el precio de la hora trabajada: ")
	preciot = float(input())
	print("Digite el porcentaje del valor de los impuestos: ")
	impue = float(input())
	# AREA DE CALCULOS // 
	salariob = (horat*preciot)
	tasas = (impue*salariob)
	salarion = (salariob-tasas)
	# AREA DE SALIDA //
	print(nom," Su salario neto es de: ",salarion," pesos")

