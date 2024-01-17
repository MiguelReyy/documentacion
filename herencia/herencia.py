# Clase padre / superclase
class Vehiculos():
    
    def __init__(self, marca, modelo):
        
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False
        self.acelerando = False
        self.frenando = False
        
    def arrancar(self):
        
        self.arrancado = True
    
    def acelerar(self):
        
        self.acelerando = True
    
    def frenar(self):
        
        self.frenando = True
        self.acelerando = False
        
    def estado(self):
        
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nArrancado:",
              self.arrancado, "\nAcelerando:", self.acelerando, "\nFrenando:", self.frenando)
        
        
# La clase moto hereda la clase vehículos
class Moto(Vehiculos):
    
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    haciendo_caballito = False
    
    def caballito(self):
        
        self.haciendo_caballito = True
        
    def estado(self):
        
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nArrancado:",
              self.arrancado, "\nAcelerando:", self.acelerando, "\nFrenando:", self.frenando,
              "\nHaciendo caballito:", self.haciendo_caballito)
        

mi_moto = Moto("Honda", "CBR")

mi_moto.arrancar()
mi_moto.acelerar()
mi_moto.caballito()

mi_moto.estado()