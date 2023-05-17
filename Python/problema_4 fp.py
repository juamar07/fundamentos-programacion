# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: programa que calcula el salario de las personas de una empresa teniendo en cuenta sus horas extras //
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 25/02/2023 // 
	# AREA DEFINICION DE VARIABLES //
	horas = float()
	preciohora = float()
	salario = float()
	# AREA DE CAPTURA DE DATOS //
	print((" Introducir horas, precio hora y nombre"))
	print(("Nombre:"))
	nombre = input()
	print(("Horas trabajadas: "))
	horas = float(input())
	print(("Precio hora: "))
	preciohora = float(input())
	# AREA DE CALCULOS // 
	if (horas<=40):
		salario = horas*preciohora
	else:
		salario = 40*preciohora+1.5*(horas-40)*preciohora
	# AREA DE SALIDA //
	print("El salario de ",nombre,"es de:",salario)

