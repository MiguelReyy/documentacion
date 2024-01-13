class Coche:
    def __init__(self, marca, modelo): # Definir el constructor
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False
    
    def arrancar(self):
        self.arrancado = True
        print("El", self.marca, self.modelo, "se ha arrancado")
        
    def parar(self):
            self.arrancado = False
            print("El", self.marca, self.modelo, "se ha parado")
            
            
laguna = Coche("Renault", "Laguna")
tesla = Coche("Tesla", "Model 3")

print(type(laguna))
print(type(tesla))

print(laguna.marca, laguna.modelo)
print(tesla.marca, tesla.modelo)

laguna.arrancar()
tesla.arrancar()

print(laguna.arrancado)
print(tesla.arrancado)

laguna.parar()
tesla.parar()

print(laguna.arrancado)
print(tesla.arrancado)