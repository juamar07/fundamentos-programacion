# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: progama que lee vel inicial, vel final y aceleraccion, y aplica la formula de tiempo // 
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 22/02/2023 // 
	# AREA DEFINICION DE VARIABLES //
	a = float()
	b = float()
	c = float()
	d = float()
	# AREA DE CAPTURA DE DATOS //
	print("Digite la velocidad inicial en m/s: ")
	a = float(input())
	print("Digite la velocidad final en m/s: ")
	b = float(input())
	print("Digite la aceleracion en m/s**2: ")
	c = float(input())
	# AREA DE CALCULOS //
	d = (b-a)/(c)
	# AREA DE SALIDA //
	print("El tiempo es de: ",d," segundos")

