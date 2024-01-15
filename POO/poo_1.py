class Coche():

    def __init__(self):
        # 4 propiedades
        self.largo_chasis = 250
        self.ancho_chasis = 120
        self.ruedas = 4
        self.encendido = False

    # 2 comportamientos
    def arrancar(self,arrancamos):
        self.encendido = arrancamos
        
        if(self.encendido) == True:
            return "El coche está encendido"
        else:
            return "El coche está apagado"


    def estado(self):
       print("El coche tiene",self.ruedas,"ruedas. Un ancho de",self.ancho_chasis,
             "y un largo de",self.largo_chasis,)



# Instanciar una clase
toyota = Coche()

print("El largo del coche es:",toyota.largo_chasis)
print("El coche tiene",toyota.ruedas,"ruedas")

print(toyota.arrancar(True))
toyota.estado()

print("\n------------A continuación creamos el segundo objeto------------"
        + "\n")

bmw = Coche()
print(f"El largo del coche es:",bmw.largo_chasis)
print("El coche tiene",bmw.ruedas,"ruedas")
print(bmw.arrancar(False))
bmw.estado()