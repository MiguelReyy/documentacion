class Empleado():

    def __init__(self, nombre, apellido, salario):

        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    def nombre_completo(self):
        
        return "{} {}".format(self.nombre, self.apellido)
    
    def listar_empleado(self):
        print(self.nombre,"\n"+self.apellido,"\n"+str(self.salario))

empleado_1 = Empleado("Alvaro", "Santamaria", 50000)
empleado_2 = Empleado("Pablo", "Jimenez", 40000)

print(empleado_1.nombre_completo())
empleado_1.listar_empleado()