class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        pass


class Perro(Animal):
    def sonido(self):
        return "¡Guau!"


class Gato(Animal):
    def sonido(self):
        return "¡Miau!"


class Pajaro(Animal):
    def sonido(self):
        return "¡Pío pío!"


# Crear instancias de las clases
perro = Perro("Firulais")
gato = Gato("Garfield")
pajaro = Pajaro("Tweety")

# Llamar al método sonido de cada instancia
print(perro.nombre + ": " + perro.sonido())
print(gato.nombre + ": " + gato.sonido())
print(pajaro.nombre + ": " + pajaro.sonido())
