# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: progama que lee tres números A, B, C y visualiza en pantalla el valor del más grande. Se supone que los tres valores son diferentes //
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 05/03/2023 // 
	# AREA DEFINICION DE VARIABLES //
	a = float()
	b = float()
	c = float()
	mayor = float()
	# Inicializar variables //
	a = 0
	b = 0
	c = 0
	# Entrada de datos //
	print("Escriba el numero A")
	a = float(input())
	print("Escriba el numero B")
	b = float(input())
	print("Escriba el numero C")
	c = float(input())
	# Procesos //
	if a>b:
		if a>c:
			print("El numero mayor es el A: ",a)
	if b>a:
		if b>c:
			print("El numero mayor es el B: ",b)
	if c>b:
		if c>a:
			print("El numero mayor es el C: ",c)

