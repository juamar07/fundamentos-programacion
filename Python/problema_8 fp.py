# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: programa que resuelve una ecuación de segundo grado -> Ax2 + Bx + C = 0  //
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 26/02/2023 // 
	# AREA DEFINICION DE VARIABLES //
	a = float()
	b = float()
	c = float()
	d = float()
	x1 = float()
	x2 = float()
	x3 = float()
	# AREA DE CAPTURA DE DATOS //
	print("Digite la variable A de la ecuacion: ")
	a = float(input())
	print("Digite la variable B de la ecuacion: ")
	b = float(input())
	print("Digite la variable C de la ecuacion: ")
	c = float(input())
	# AREA DE CALCULOS // 
	d = (b**2)-(4*a*c)
	d = (d**0.5)
	if d<0:
		# AREA DE SALIDA //
		print("error, vuelva a intentarlo con un numero mayor")
	if d>=0:
		x3 = (-b)/(2*a)
		# AREA DE SALIDA //
		print("el resultado de la ecuacion es: ",x3)
	if d>0:
		x1 = (-b+d)/(2*a)
		x2 = (-b-d)/(2*a)
		# AREA DE SALIDA //
		print("el resultado de la ecuacion en X1 = ",x1," y de X2 = ",x2)

