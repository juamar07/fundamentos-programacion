# how to calculate a factorial?
fact = 1 
multi = 1
mdr = 10 
mdo = 1 
mdr1 = 10 
mdo1 = 1 
for x in range (1,65):
    multi = multi * x 
    print(f"El factorial de {x} es: {multi}")

# tabla de multiplicar 

mdo = 1 
mdr = 10 
mdo = int (input('digite tabla: '))
for x in range (10):
    for y in range (1,mdr+1):
      res = x * mdo 
    print (res)

# Tablas de multiplicar 

mdo1 = 1
mdr1 = 10 
for i in range (1,11):
    print("Tabla ", mdo1)
    for i in range (1,mdr1+1):
        res1 = i * mdo1 
        print(mdo1,"*", i, "=", res1)
