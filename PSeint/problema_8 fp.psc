Algoritmo problema_8
	// Descripcion: programa que resuelve una ecuación de segundo grado -> Ax2 + Bx + C = 0  //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 26/02/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir a,b,c,d,x1,x2,x3 Como Real
	// AREA DE CAPTURA DE DATOS //
	Escribir 'Digite la variable A de la ecuacion: '
	Leer a
	Escribir 'Digite la variable B de la ecuacion: '
	Leer b
	Escribir 'Digite la variable C de la ecuacion: '
	Leer c
	// AREA DE CALCULOS // 
	d <- (b^2)-(4*a*c)
	d <- (d^0.5)
	Si d<0 Entonces
		// AREA DE SALIDA //
		Escribir 'error, vuelva a intentarlo con un numero mayor'
	FinSi
	Si d>=0 Entonces
		x3 <- (-b)/(2*a)
		// AREA DE SALIDA //
		Escribir 'el resultado de la ecuacion es: ',x3
	FinSi
	Si d>0 Entonces
		x1 <- (-b+d)/(2*a)
		x2 <- (-b-d)/(2*a)
		// AREA DE SALIDA //
		Escribir 'el resultado de la ecuacion en X1 = ',x1,' y de X2 = ',x2
	FinSi
FinAlgoritmo
