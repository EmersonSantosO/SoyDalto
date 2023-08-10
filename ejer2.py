class Masmorra:
    lista_masmorras = []

    def __init__(self, nombre_masmorra, nivel_masmorra) -> None:
        self.nombre_masmorra = nombre_masmorra
        self.nivel_masmorra = nivel_masmorra
        Masmorra.lista_masmorras.append(self)

    @classmethod
    def mostrar_lista(cls):
        for masmorra in cls.lista_masmorras:
            print(f"{masmorra}")

    def __str__(self) -> str:
        return f"Nombre:{self.nombre_masmorra}, Nivel:{self.nivel_masmorra}"

    def mostrar_masmorra(self):
        print(f"Nombre:{self.nombre_masmorra}, Nivel:{self.nivel_masmorra}")


class Monstruo(Masmorra):
    lista_monstruos = []

    def __init__(self, nombre_masmorra, nivel_masmorra, nombre, vida, drop, zona) -> None:
        Masmorra.__init__(self, nombre_masmorra, nivel_masmorra)
        self.nombre = nombre
        self.vida = vida
        self.drop = drop
        self.zona = zona
        Monstruo.lista_monstruos.append(self)

    def __str__(self) -> str:
        return f"Nombre:{self.nombre}, Vida:{self.vida}, Drop:{self.drop}, Zona:{self.zona}"

    @classmethod
    def mostrar_lista(cls):
        for monstruo in cls.lista_monstruos:
            print(f"{monstruo}")

    def mostrar_monstruo(self):
        print(
            f"Nombre:{self.nombre}, Vida:{self.vida}, Drop:{self.drop}, Zona:{self.zona}")


masmorra1 = Masmorra("Jalato", 50)
masmorra2 = Masmorra("Bwork", 100)
masmorra3 = Masmorra("Tofu", 150)
masmorra4 = Masmorra("Bouftou", 200)
masmorra5 = Masmorra("Tiwabbit", 250)
masmorra1.mostrar_masmorra()
Masmorra.mostrar_lista()
monstruo1 = Monstruo("Jalato", 50, "Jalato", 100, "Cuero", "Astrub")
monstruo2 = Monstruo("Bwork", 100, "Bwork", 200, "Madera", "Bonta")
monstruo3 = Monstruo("Tofu", 150, "Tofu", 300, "Pluma", "Amakna")
monstruo4 = Monstruo("Bouftou", 200, "Bouftou", 400, "Lana", "Brakmar")
monstruo5 = Monstruo("Tiwabbit", 250, "Tiwabbit", 500, "Zanahoria", "Pandala")
Monstruo.mostrar_lista()
monstruo1.mostrar_monstruo()
