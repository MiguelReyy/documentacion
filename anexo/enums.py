from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# Acceder a los miembros de la enumeración
print(Color.RED)  # Output: Color.RED

# Comparación de enumeraciones
if Color.RED == Color.GREEN:
    print("Esto no se imprimirá.")
else:
    print("Los colores son diferentes.")

# Iteración sobre los miembros de la enumeración
for i in Color:
    print(i)

# Mismo output
print(Color["RED"].value)
print(Color.RED.value)

# Crea una lista de la clase enum
lista = [i for i in Color]
print(lista)
for i in lista:
    print(i.value)