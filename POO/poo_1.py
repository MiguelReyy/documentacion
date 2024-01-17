class Coche():

    def __init__(self):
        # 4 propiedades
        self.largo_chasis = 250     # Atributo público
        self.ancho_chasis = 120
        self._ruedas = 4       # Atributo privado
        self.encendido = False

    # 2 comportamientos
    def arrancar(self,arrancamos):
        self.encendido = arrancamos
        
        if(self.encendido) == True:
            check = self.chequeo()

        if(self.encendido and check) == True:
            return "El coche está encendido"
        elif(self.encendido and check == False):
            return "Algo va mal, no se puede arrancar"
        else:
            return "El coche está apagado"


    def estado(self):
       print("El coche tiene",self._ruedas,"ruedas. Un ancho de",self.ancho_chasis,
             "y un largo de",self.largo_chasis,)

    def chequeo(self):
        print('Realizando chequeo interno...')

        self.gasolina = "OK"
        self.aceite = "OK"
        self.puertas = "Cerradas"

        if(self.gasolina == "OK" and self.aceite == "OK" and self.puertas == "Cerradas"):
            return True
        else:
            return False

# Instanciar una clase
toyota = Coche()

print("El largo del coche es:",toyota.largo_chasis)
print("El coche tiene",toyota._ruedas,"ruedas")

print(toyota.arrancar(True))
print(toyota.chequeo())
toyota.estado()

print("\n------------A continuación creamos el segundo objeto------------"
        + "\n")

bmw = Coche()
print(f"El largo del coche es:",bmw.largo_chasis)
print("El coche tiene",bmw._ruedas,"ruedas")
print(bmw.arrancar(False))
bmw.ruedas = 2
bmw.estado()