# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición

my_list = list()
my_other_list = []

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))
print(type(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0]) #imprimir elemento determinado de la lista
print(my_other_list.index("Brais")) #index es para saber si esta en la lista

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev")
print(my_other_list)

my_other_list.insert(1, "Rojo") #inser en (indice, elemento)
print(my_other_list)

# Añadir varios elementos a la lista
my_other_list.extend([False, 2024])

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)


print(my_list.pop(2))
print(my_list)

del my_list[2] #eliminar el elemento en la posicion 2, recuerda que el 0 se cuenta como posicionm, no es 1 directamente
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)


# Sublistas

print(my_new_list[1:3])