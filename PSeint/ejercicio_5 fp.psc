Algoritmo ejercicio_5
	// Descripcion: progama que pregunta qué día de la semana fue el día 1 del mes actual y calcula que día de la semana es hoy //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 05/03/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir dia,d1 Como Entero
	Definir dia1 Como Caracter
	// Entrada de datos //
	Escribir ('El dia 1 del mes fue (l,m,x,j,v,s,d): ')
	Leer dia1
	Segun dia1  Hacer
		'l':
			// Procesos //
			d1 <- 0
		'm':
			d1 <- 1
		'x':
			d1 <- 2
		'j':
			d1 <- 3
		'v':
			d1 <- 4
		's':
			d1 <- 5
		'd':
			d1 <- 6
			// SiNo
			d1 <- -40
	FinSegun
	Escribir ('Diga el dia ')
	// Salida de datos //
	Leer dia
	dia <- dia+d1
	Segun dia MOD 7  Hacer
		1:
			Escribir ('Lunes')
		2:
			Escribir ('Martes')
		3:
			Escribir ('Miercoles')
		4:
			Escribir ('Jueves')
		5:
			Escribir ('Viernes')
		6:
			Escribir ('Sabado')
		0:
			Escribir ('Domingo')
	FinSegun
FinAlgoritmo
