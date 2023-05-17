# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: programa recibe tres números enteros e imprime el mayor de ellos.  //
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 26/02/2023 // 
	# AREA DEFINICION DE VARIABLES //
	a = int()
	b = int()
	c = int()
	d = int()
	# AREA DE CAPTURA DE DATOS //
	print("Digite el primer numero: ")
	a = int(input())
	print("Digite el segundo numero: ")
	b = int(input())
	print("Digite el tercer numero: ")
	c = int(input())
	# AREA DE CALCULOS // 
	if a>b and b>c:
		print("el numero mayor es el primero:",a)
		if b>a and a>c:
			print("el numero mayor es el segundo:",b)
		else:
			print("el numero mayor es el tercero:",c)

