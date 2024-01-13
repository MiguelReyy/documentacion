diccionario = {
    "nombre": "Alvaro",
    "sexo": "Hombre",
    "altura": 1.85,
    "edad": 18
}

# Devuelve las claves (sirve para iterar)
claves = diccionario.keys()
print(claves)

# Devuelve el valor del key introducido (si no encuentra devuelve excepción)
claves = diccionario["altura"]
print(claves)

# Devuelve el valor del key introducido (si no encuentra devuelve None)
claves = diccionario.get("santamaria")
print(claves)

# Eliminar todo el diccionario
diccionario.clear

# Eliminar un elemento del diccionario
diccionario.pop("nombre")

# Obteniendo un elemento iterable
diccionario_iterable = diccionario.items()