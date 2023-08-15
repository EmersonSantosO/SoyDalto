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
