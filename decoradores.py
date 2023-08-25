def modificar_funcion(funcion):
    def modificar():
        funcion()
        print("Chao")
    return modificar


@modificar_funcion
def saludo():
    print("Hola ")


saludo()


class persona:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre


persona1 = persona("xd")
persona1.nombre
persona1.nombre = "asd"

persona1.nombre
