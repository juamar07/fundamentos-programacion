Algoritmo ejercicio_7
	Definir a,b,c,d,x1,x2,r,i Como Real
	Escribir 'escriba el coeficiente equivalente A: '
	Leer a
	Escribir 'escriba el coeficiente equivalente B: '
	Leer b
	Escribir 'escriba el coeficiente equivalente C: '
	Leer c
	Si a=0 Entonces
		Escribir ('No es ecuacion de segundo grado')
	SiNo
		d <- b*b-4*a*c
		Si d=0 Entonces
			x1 <- -b/(2*a)
			x2 <- x1
			Escribir x1,x2
			Si d>0 Entonces
				x1 <- (-b+(d)^0.5)/(2*a)
				x2 <- (-b-(d)^0.5)/(2*a)
				Escribir x1,x2
			SiNo
				r <- (-b)/(2*a)
				i <- (abs(d))^0.5/(2*a)
				Escribir r,'+',i,'i'
				Escribir r,'-',i,'i'
			FinSi
		FinSi
	FinSi
FinAlgoritmo
