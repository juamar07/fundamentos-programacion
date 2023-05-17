Algoritmo ejercicio_2
	// Descripcion: progama que calcula la nomina de un empleado //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 06/03/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir v_nomemp Como Caracter
	Definir v_horsentra,v_valhor,v_valhorext,v_valhornor Como Entero
	Definir v_valimp,v_suebas,v_suepag Como Real
	// Inicializacion de variables //
	v_nomemp <- ''
	v_horsentra <- 0
	v_valhor <- 0
	v_valhorext <- 0
	v_valhornor <- 0
	v_valimp <- 0.0
	v_suebas <- 0.0
	v_suepag <- 0.0
	// Entrada de datos //
	Escribir 'Escriba el nombre del empleado: '
	Leer v_nomemp
	Escribir 'Digite las horas trabajadas semanales: '
	Leer v_horsentra
	Escribir 'Digite el valor de la hora trabajada: '
	Leer v_valhor
	// Area de procesos // 
	Si v_horsentra<35 Entonces
		v_suebas <- v_horsentra*v_valhor
	SiNo
		v_suebas <- 35*v_valhor+(v_horsentra-35)*v_valhor*1.5
	FinSi
	Si v_suebas>=300000 Y v_suebas<=400000 Entonces
		v_valimp <- (v_suebas-300000)*0.20
	SiNo
		Si v_suebas>400000 Entonces
			v_valimp <- (100000)*0.2+(v_suebas-400000)*0.3
		FinSi
	FinSi
	v_suepag <- v_suebas-v_valimp
	Escribir v_nomemp,' su salario final es de: ',v_suepag
FinAlgoritmo
