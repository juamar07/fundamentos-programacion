# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	a = float()
	b = float()
	c = float()
	d = float()
	x1 = float()
	x2 = float()
	r = float()
	i = float()
	print("escriba el coeficiente equivalente A: ")
	a = float(input())
	print("escriba el coeficiente equivalente B: ")
	b = float(input())
	print("escriba el coeficiente equivalente C: ")
	c = float(input())
	if a==0:
		print(("No es ecuacion de segundo grado"))
	else:
		d = b*b-4*a*c
		if d==0:
			x1 = -b/(2*a)
			x2 = x1
			print(x1,x2)
			if d>0:
				x1 = (-b+(d)**0.5)/(2*a)
				x2 = (-b-(d)**0.5)/(2*a)
				print(x1,x2)
			else:
				r = (-b)/(2*a)
				i = (abs(d))**0.5/(2*a)
				print(r,"+",i,"i")
				print(r,"-",i,"i")

