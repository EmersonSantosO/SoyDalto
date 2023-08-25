class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        Persona.__init__(self, nombre, edad)
        self.carrera = carrera

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}"

    def mostrar_datos(self):
        print(
            f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}")


def modificar_funcion(funcion):
    def modificar():
        funcion()
        print("Chao")
    return modificar


@modificar_funcion
def saludo():
    print("Hola ")


saludo()
