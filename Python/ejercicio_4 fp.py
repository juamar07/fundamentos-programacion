# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	dia = int()
	print("digite el numero del dia de la semana: ")
	dia = int(input())
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

