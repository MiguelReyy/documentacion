class Coche():

    # 4 propiedades
    largo_chasis = 250
    ancho_chasis = 120
    ruedas = 4
    encendido = False

    # 2 comportamientos
    def arrancar(self):
        self.encendido = True   # self. significa "toyota.encendido = True"

    def estado(self):
        if(self.encendido) == True:
            return "El coche está encendido"
        else:
            return "El coche está apagado"

# Instanciar una clase
toyota = Coche()

print("El largo del coche es:",toyota.largo_chasis)
print("El coche tiene",toyota.ruedas,"ruedas")

toyota.arrancar()
print(toyota.estado())
