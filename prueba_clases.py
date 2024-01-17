class Vehiculo():

    def __init__(self, marca):
        
        self.marca = marca
        self.encendido = "apagado"

    def arrancar(self):

        self.encendido = "encendido"

    def estado(self):

        print("\nEl", self.marca, "está", self.encendido)


mercedes = Vehiculo("Mercedes")

while True:
        
        respuesta1 = input("\nQuieres encender el coche? (s/n): ")

        if respuesta1 in ["s", "n"]:
            if respuesta1 == "s":
                print("\nArrancando...")
                mercedes.arrancar()
                break
            else:
                break
        else:
            print("\nTecla incorrecta")
            continue

mercedes.estado()