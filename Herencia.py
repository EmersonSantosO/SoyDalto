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


estudiante1 = Estudiante("Juan", 20, "Informatica")
estudiante1.mostrar_datos()
