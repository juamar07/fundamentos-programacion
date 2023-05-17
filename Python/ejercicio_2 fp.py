# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: progama que calcula la nomina de un empleado //
	# Desarrollado por: Juan Martin Betancur //
	# Version 1.0 //
	# Fecha ultima actualizacion: 06/03/2023 // 
	# AREA DEFINICION DE VARIABLES //
	v_nomemp = str()
	v_horsentra = int()
	v_valhor = int()
	v_valhorext = int()
	v_valhornor = int()
	v_valimp = float()
	v_suebas = float()
	v_suepag = float()
	# Inicializacion de variables //
	v_nomemp = ""
	v_horsentra = 0
	v_valhor = 0
	v_valhorext = 0
	v_valhornor = 0
	v_valimp = 0.0
	v_suebas = 0.0
	v_suepag = 0.0
	# Entrada de datos //
	print("Escriba el nombre del empleado: ")
	v_nomemp = input()
	print("Digite las horas trabajadas semanales: ")
	v_horsentra = int(input())
	print("Digite el valor de la hora trabajada: ")
	v_valhor = int(input())
	# Area de procesos // 
	if v_horsentra<35:
		v_suebas = v_horsentra*v_valhor
	else:
		v_suebas = 35*v_valhor+(v_horsentra-35)*v_valhor*1.5
	if v_suebas>=300000 and v_suebas<=400000:
		v_valimp = (v_suebas-300000)*0.20
	else:
		if v_suebas>400000:
			v_valimp = (100000)*0.2+(v_suebas-400000)*0.3
	v_suepag = v_suebas-v_valimp
	print(v_nomemp," su salario final es de: ",v_suepag)

