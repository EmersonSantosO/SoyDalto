class A():
    pass


class B(A):
    pass


class C(A):
    pass


class D(C, A):
    pass


class E(D, B):
    pass


class F(B, A):
    pass


class G(E, F):
    pass


print(G.mro())


def recorrer(**kwargs):
    for k, v in kwargs.items():
        print(f"Key:{k}Valor:{v}")


recorrer(hola="hello", chao="bye")


bala = -10
misil = -1000


def resistencia(*args):
    escudo = 1000
    for v in args:
        escudo += v
    return escudo


resistencia(bala, misil, bala, misil)


def mostrar_celulares(**kwargs):
    for key, value in kwargs.items():
        print(f"Celular:{key} Modelo: {value}")


mostrar_celulares(samsung="a20", apple="iphone4")


def suma(*args):
    resultado = 0
    for n in args:
        resultado += n
    return resultado


suma(1, 2, 4, 1, 1000, 2)


class Animales:
    lista_animales = []

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        Animales.lista_animales.append(self)

    def __str__(self) -> str:
        return self.nombre

    @classmethod
    def mostrar_lista(cls):
        for animal in cls.lista_animales:
            print(f"Animal:{animal}")

    def comer(self):
        return f"{self.nombre} Comiendo"

    @staticmethod
    def defecar():
        return "Defecando"


animal1 = Animales("Perro")
animal2 = Animales("Gato")

animal1.defecar()


class Humano(Animales):
    def __init__(self, nombre, apellido) -> None:
        super().__init__(nombre)
        self.apellido = apellido

    def mostrar_datos(self):
        return f"{self.nombre} {self.apellido}"


pepito = Humano("pepe", "zuazo")
pepito.mostrar_datos()


def suma(numero):
    if numero == 0:
        raise ValueError("XD")
    try:

        resultado = 0
        resultado += (numero)

    except:
        return f"no es un numero: {numero} xd"
    else:
        return f"El resultado es: {resultado}"


suma(1)
