Algoritmo ejercicio_3
	// Descripcion: progama lee los lados de un triangulo y da su area //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	// Fecha ultima actualizacion: 27/02/2023 // 
	// AREA DEFINICION DE VARIABLES //
	Definir a,b,c,p,area Como Real
	// Entrada de datos //
	Escribir 'Escriba el primer lado del triangulo: '
	Leer a
	Escribir 'Escriba el segundo lado del triangulo: '
	Leer b
	Escribir 'Escriba el tercer lado del triangulo: '
	Leer c
	// Procesos //
	p <- (a+b+c)/2
	Si (p>a) Y (p>b) Y (p>c) Entonces
		area <- (p*(p-a)*(p-b)*(p-c))^0.5
		Escribir 'El area del triangulo es: ',area
	SiNo
		Escribir ('No es un triangulo')
	FinSi
FinAlgoritmo
