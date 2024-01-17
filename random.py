import random

baraja = {
    "as": 1,
    "dos": 2,
    "tres": 3
}

lista_cartas = list(baraja.values())
x = random.choice(lista_cartas)

print(x)