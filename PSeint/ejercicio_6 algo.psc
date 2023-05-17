Algoritmo ejercicio_6
	
	// Area de documentacion //
	// Programa para convertir metros sobre segundo a kilometros por hora //
	// Desarrollado por: Juan Martin Betancur //
	// Version 1.0 //
	
	// Area de definicion de variables //
	
	Definir v_metseg Como Real // Variable de entrada que almacena los metros sobre segundo //
	Definir v_kilhor Como Real // Variable de entrada que almacena los kilometros por hora //
	Definir c_faccon Como Real // Constante que almacena el factor de conversion //
	
	// Inicializacion de variables //
	
	v_metseg=0.0
	v_kilhor=0.0
	c_faccon=3.6
	
	// Area de entradas //
	
	Escribir 'digite metros sobre segundo: '; Leer v_metseg;
	
	// Area de procesos //
	
	v_kilhor=v_metseg*c_faccon
	
	// Area de salidas //
	
	Escribir 'la convesion es: ',v_kilhor
	
	
	
	
	
	
FinAlgoritmo
