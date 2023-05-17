# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: progama que pregunta que dia de la semana fue el dia 1 del mes actual y calcula que dia de la semana es hoy //
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 05/03/2023 // 
	# AREA DEFINICION DE VARIABLES //
	dia = int()
	d1 = int()
	dia1 = str()
	# Entrada de datos //
	print(("El dia 1 del mes fue (l,m,x,j,v,s,d): "))
	dia1 = input()
	if dia1=="l":
		# Procesos //
		d1 = 0
	elif dia1=="m":
		d1 = 1
	elif dia1=="x":
		d1 = 2
	elif dia1=="j":
		d1 = 3
	elif dia1=="v":
		d1 = 4
	elif dia1=="s":
		d1 = 5
	elif dia1=="d":
		d1 = 6
		# SiNo
		d1 = -40
	print(("Digite el numero del dia de hoy: "))
	# Salida de datos //
	dia = int(input())
	dia = dia+d1
	if dia%7==1:
		print(("Lunes"))
	elif dia%7==2:
		print(("Martes"))
	elif dia%7==3:
		print(("Miercoles"))
	elif dia%7==4:
		print(("Jueves"))
	elif dia%7==5:
		print(("Viernes"))
	elif dia%7==6:
		print(("Sabado"))
	elif dia%7==0:
		print(("Domingo"))

