cadena1 = "Hola soy Alvaro"
cadena2 = "bienvenido bro"

# Convierte a mayúsculas
mayusc = cadena1.upper()

# Convierte a minúsculas
minusc = cadena1.lower()

# Primera letra en mayúsculas
primer_letra_mayusc = cadena2.capitalize()

# Busca una cadena en otra cadena (si no hay resultado devuelve -1)
busqueda_find = cadena1.find("a")   # Devuelve posicion en la cadena
busqueda_find = cadena1.find("Hola")    # Devuelve posicion en la cadena de la primera letra

# Busca una cadena en otra cadena (si no hay resultados devuelve una excepción)
busqueda_index = cadena1.index("d")

# Si es numerico, devuelve True, si no, False
es_numerico = cadena1.isnumeric()

print(es_numerico)