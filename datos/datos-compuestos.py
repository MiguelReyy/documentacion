
# Creando una lista (se pueden modificar)
lista = ["Alvaro","Hombre",True,1.85]

# Creando una tupla (no se pueden modificar)
tupla = ("Alvaro","Hombre",True,1.85)

# Esto es válido
lista[3] = 2

# Esto no es válido
"""tupla[3] = 2"""

print(lista[3])
print(tupla[3])
print(lista[0:2])

# Creando un conjunto (no se pueden modificar, no se accede por índice, no almacena duplicados)
conjunto = {"Alvaro","Hombre",True,1.85,"Alvaro"}

print(conjunto)

# Creando un diccionario (key ~ value)
diccionario = {
    "nombre": "Alvaro",
    "sexo": "Hombre",
    "altura": 1.85,
    "edad": 18
}

print(diccionario["nombre"])