# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: progama lee los lados de un triangulo y da su area //
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 27/02/2023 // 
	# AREA DEFINICION DE VARIABLES //
	a = float()
	b = float()
	c = float()
	p = float()
	area = float()
	# Entrada de datos //
	print("Escriba el primer lado del triangulo: ")
	a = float(input())
	print("Escriba el segundo lado del triangulo: ")
	b = float(input())
	print("Escriba el tercer lado del triangulo: ")
	c = float(input())
	# Procesos //
	p = (a+b+c)/2
	if (p>a) and (p>b) and (p>c):
		area = (p*(p-a)*(p-b)*(p-c))**0.5
		print("El area del triangulo es: ",area)
	else:
		print(("No es un triangulo"))

