# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: progama que lee vel inicial, vel final y tiempo, y aplica la formula de aceleracion // 
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 22/02/2023 // 
	# AREA DEFINICION DE VARIABLES //
	a = float()
	b = float()
	c = float()
	d = float()
	e = float()
	f = float()
	# Inicializacion de variables //
	f = 0.5
	# AREA DE CAPTURA DE DATOS //
	print("Digite la velocidad inicial en m/s")
	a = float(input())
	print("Digite la velocidad final en m/s")
	b = float(input())
	print("Digite el tiempo en s")
	c = float(input())
	# AREA DE CALCULOS //
	d = (b-a)/(c)
	e = (a*c)+(f)*(d*(c*c))
	# AREA DE SALIDA //
	print("la aceleracion es de: ",d," m/s**2")
	print("la distancia es de: ",e," m")

