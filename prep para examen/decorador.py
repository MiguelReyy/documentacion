def decorador(funcion):

    def funcioninterior():

        print("Antes de llamar a la función")

        funcion()  # Llamar a la función original

        print("Después de llamar a la función")

    return funcioninterior

@decorador
def funcion_a_decorar():

    print("¡Esta es la función que será decorada!")

funcion_a_decorar()

print("----------------------------------")


def decorador2(funcion2):

    def funcioninterior2(*args): #* args significa que le podemos pasar un numero indeterminado de parametros

        print("decorado antes")

        funcion2(*args)  # Llamar a la función original

        print("decorado despues")

    return funcioninterior2

@decorador2
def suma(n1, n2):

    print(n1 + n2)

suma(2, 3)


print("----------------------------------")

def decorador3(funcion3):

    def funcioninterior3(**kwargs): # **kwargs significa que le podemos pasar un dato tipo clave valor

        print("decorador pre potencia")

        funcion3(**kwargs)  # Llamar a la función original

        print("decorador post potencia")

    return funcioninterior3

@decorador3
def potencia(base, exponente):

    print(pow(base, exponente))

potencia(base=5, exponente=4)