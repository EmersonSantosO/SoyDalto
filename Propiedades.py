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


class Transport:
    def __init__(self, name, speed, type):
        self.name = name
        self.speed = speed
        self.type = type

    def __str__(self):
        return self.__all__

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, newName):
        self.name = newName


car = Transport("car", 100, "land")
car.name
car.name = "car2"
car.name


class Plane:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Configuracion:
    def __init__(self, **kwargs):
        self.valores = kwargs

    def __str__(self) -> str:
        return self.valores


configuracion1 = Configuracion(color="rojo", tamaño="mediano")
configuracion2 = Configuracion(temperatura=25, idioma="español")
configuracion1.valores


class Animal:
    def __init__(self, name, size, *args) -> None:
        self.name = name
        self.size = size
        self.ability = list(args)

    def add_ability(self, ability):
        self.ability.append(ability)

    def view_skills(self):
        print(f"Name = {self.name}")
        print(f"Size = {self.size}")
        print("Skills = ")
        for s in self.ability:
            print(f"{s}")


perro = Animal("Dog", "1 metro", "corre", "salta", "ladra")

perro.view_skills()
