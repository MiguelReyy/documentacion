# Creando una lista con list()
lista = list(["hola","alvaro",34])

# Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

# Añadir un elemento al final de la lista
lista.append("hombre")

# Añade un elemento a la lista en un índice específico
lista.insert(2, "santamaria")   # 18 es el 2 y 34 es el 3 ahora

# Añadir varios elementos a la lista
lista.extend([False, 2024])

# Eliminar un elemento de la lista (por su índice)
lista.pop(0)
lista.pop(-1)   # Elimina el último elemento, etc

# Elimina un elemento de la lista por su valor
lista.remove("alvaro")

# Elimina todos los elementos de la lista
lista.clear()

# Ordena los elementos de la lista de forma ascendente (no funciona con str)
lista.sort()

# Invierte la posición de los elementos de una lista
lista.reverse()

# Verificar si un elemento se encuantra en la lista
elemento_encontrado = lista.index(34)

