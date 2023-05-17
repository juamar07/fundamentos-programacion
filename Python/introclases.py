# Programcion orientada a objetos 

class Persona:

    def inicializar (self,nom):
        self.nombre = nom

    def imprimir(self):
        print ("Nombre", self.nombre)

# Bloque principal

persona1 = Persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Juan")
persona2.imprimir()


class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado")
        self.sueldo = float(input("Ingrese el salario del empleado"))

        def escribir (self):
            print ("Nombre", self.nombre)
        
        def paga_impuestos (self):
            if self.sueldo > 3000:
                print("Debe pagar impuestos")
            else:
                print("No paga impuestos")

empleado1 = Empleado()
empleado1.escribir()
empleado1.paga_impuestos()
