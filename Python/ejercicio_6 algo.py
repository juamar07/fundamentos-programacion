# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de documentacion //
	# Programa para convertir metros sobre segundo a kilometros por hora //
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Area de definicion de variables //
	# Variable de entrada que almacena los metros sobre segundo //
	v_metseg = float()
	# Variable de entrada que almacena los kilometros por hora //
	v_kilhor = float()
	# Constante que almacena el factor de conversion //
	c_faccon = float()
	# Inicializacion de variables //
	v_metseg = 0.0
	v_kilhor = 0.0
	c_faccon = 3.6
	# Area de entradas //
	print("digite metros sobre segundo: ")
	v_metseg = float(input())
	# Area de procesos //
	v_kilhor = v_metseg*c_faccon
	# Area de salidas //
	print("la convesion es: ",v_kilhor)

