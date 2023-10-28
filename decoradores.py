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

class animales:
    lista_animales = []

    def __init__(self, nombre, especie) -> None:
        self.nombre = nombre
        self.especie = especie
        animales.lista_animales.append(self)

    def __str__(self) -> str:
        return f"{self.nombre}{self.especie}"

    @classmethod
    def mostrar_animales(cls):
        for animal in cls.lista_animales:
            print(f"Animal:{animal}")


nombre1 = "perro"
especie1 = "canido"
animal1 = animales(nombre1, especie1)
animales.mostrar_animales()