
class Libro:
    def __init__(self, titulo, autor, año_publicacion, cantidad_ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.cantidad_ejemplares = cantidad_ejemplares
        self.libros_prestados = []

    def mostrar_informacion(self):
        print(
            "\nTítulo:", self.titulo,
            "\nAutor:", self.autor,
            "\nAño de publicación:", self.año_publicacion,
            "\nNº de ejemplares:", self.cantidad_ejemplares
        )

    def prestar_libro(self):
        if self.cantidad_ejemplares > 0:
            self.cantidad_ejemplares -= 1
            self.libros_prestados.append(self.titulo)
            print(f"\nSe prestó el libro '{self.titulo}'")
        else:
            print(f"\nLo siento, no hay ejemplares disponibles de '{self.titulo}'")

    def devolver_libro(self):
        if self.titulo in self.libros_prestados:
            self.cantidad_ejemplares += 1
            self.libros_prestados.remove(self.titulo)
            print(f"\nSe ha devuelto el libro '{self.titulo}'")
        else:
            print(f"\nNo se puede devolver '{self.titulo}'. No hay ningún libro prestado.")


def elegir():

    while True:
        eleccion = input("\nPara pedir un libro pulsa 'p', para devolver pulsa 'd', para salir pulsa 's': ")

        if eleccion == "s":
            exit()
        elif eleccion == "p":
            coger_libro()
            break
        elif eleccion == "d":
            dejar_libro()
            break
        else:
            print("\nPor favor, introduce 'p', 'd' o 's'")


def coger_libro():

    while True:
        eleccion_2 = input("\n¿Qué libro quieres coger? Opciones: 'Don Quijote de la Mancha'(1), 'La Tabla de Flandes'(2): ")

        try:
            eleccion_2 = int(eleccion_2)

            if eleccion_2 in [1, 2]:
                if eleccion_2 == 1:
                    el_quijote.prestar_libro()
                else:
                    tabla_de_flandes.prestar_libro()
                break
            else:
                print("\nPor favor, introduce '1' o '2'")

        except ValueError:
            print("\nPor favor, introduce un número válido.")


def dejar_libro():

    while True:
        eleccion_2 = input("\n¿Qué libro quieres devolver? Opciones: 'Don Quijote de la Mancha'(1), 'La Tabla de Flandes'(2): ")

        try:
            eleccion_2 = int(eleccion_2)

            if eleccion_2 in [1, 2]:
                if eleccion_2 == 1:
                    el_quijote.devolver_libro()
                else:
                    tabla_de_flandes.devolver_libro()
                break
            else:
                print("\nPor favor, introduce '1' o '2'")

        except ValueError:
            print("\nPor favor, introduce un número válido.")

if __name__ == "__main__":
    # Creamos las instancias
    el_quijote = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, 5)
    tabla_de_flandes = Libro("La Tabla de Flandes", "Arturo Pérez-Reverte", 1990, 3)

    # Bucle principal
    while True:
        titulo = "LIBROS"
        print("\n" + titulo + "\n" + "-" * len(titulo))
        el_quijote.mostrar_informacion()
        tabla_de_flandes.mostrar_informacion()
        elegir()