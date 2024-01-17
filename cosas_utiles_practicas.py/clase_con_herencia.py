class vehiculo:
    def __init__(self, price, tipo, matricula):
        self.price = price #se pone igual
        self.tipo = tipo
        self.matricula = matricula
    
    def presentarse (self): #se pasa el self obligatorio
        print(f"Este coche es un {self.tipo} y tiene la matricula {self.matricula}")

BMW = vehiculo(35, "tractor", "AAA1234")

BMW.presentarse()

print(BMW.price)

class tractor(vehiculo):
    pass #aunque este vacia esta heredando los elementos y atributos de la clase vehiculo, esto se utiliza si no vas a añadir ninguna propiedad extra a la clase

tractor = tractor(56, "coche", "bbb1234")
tractor.presentarse()

class coche(vehiculo):
    def __init__(self,price, tipo, matricula, tiporuedas, gastomensual):
        super().__init__(price, tipo, matricula) #super hace referencia de la clase padre (vehiculo)
        self.tiporuedas = tiporuedas
        self.gastomensual = gastomensual
    
    def calcular_precio_anual(self): #se pasa el self obligatorio
        
        return self.gastomensual*12

coche = coche(56, "coche", "bbb1234", "ruedas de lluvias", 150)
coche.presentarse()
print(coche.calcular_precio_anual(), "litros")

class moto(vehiculo):
    def __init__(self, price, tipo, matricula, cilindrada) :
        super().__init__(price, tipo, matricula)
        self.cilindrada = cilindrada
    
    def describirse(self):
        print(f"tengo una cilindrada de {self.cilindrada} y cuesto {self.price} euros")

moto = moto(25, "moto", "ccc1234", 125)
moto.describirse()