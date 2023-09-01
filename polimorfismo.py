class Perro:
    def sonido(self):
        return "guaof"


class Gato:
    def sonido(self):
        return "miau"


def hacer_sonido(animal):
    return print(animal.sonido())


hacer_sonido(Perro())
