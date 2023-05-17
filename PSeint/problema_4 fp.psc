Algoritmo problema_4
	// Descripcion: programa que calcula el salario de las personas de una empresa teniendo en cuenta sus horas extras //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 25/02/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir horas,preciohora,salario Como Real
	// AREA DE CAPTURA DE DATOS //
	Escribir (' Introducir horas, precio hora y nombre')
	Escribir ('Nombre:')
	Leer nombre
	Escribir ('Horas trabajadas: ')
	Leer horas
	Escribir ('Precio hora: ')
	Leer preciohora
	// AREA DE CALCULOS // 
	Si (horas<=40) Entonces
		salario <- horas*preciohora
	SiNo
		salario <- 40*preciohora+1.5*(horas-40)*preciohora
	FinSi
	// AREA DE SALIDA //
	Escribir 'El salario de ',nombre,'es de:',salario
FinAlgoritmo
