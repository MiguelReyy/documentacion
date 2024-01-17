class Persona():
    def __init__(self, nombre, apellido_paterno, apellido_materno):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno

    def mostrar_nombre_completo(self):
        txt = "{0} {1} {2}"
        return txt.format(self.apellido_paterno, self.apellido_materno, self.nombre)

class Estudiante(Persona):
    def __init__(self, nombre, apellido_paterno, apellido_materno, profesion):
        super().__init__(nombre, apellido_paterno, apellido_materno)
        self.profesion = profesion

estudiante_1 = Estudiante("Alvaro", "Santamaria", "Anton", "Ingeniero")
print(estudiante_1.mostrar_nombre_completo())
print(estudiante_1.profesion)
