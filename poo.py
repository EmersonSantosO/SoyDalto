class Dog:
    dogs = []

    def __init__(self, age, weight, race, name) -> None:
        self.age = age
        self.weight = weight
        self.race = race
        self.name = name
        Dog.dogs.append(self)

    def __str__(self):
        return f"Age:{self.age},Weight:{self.weight},Race:{self.race},Name:{self.name}"

    @classmethod
    def view_list(cls):
        for dog in cls.dogs:
            print(f"Present Dates:{dog}")


dog1 = Dog(12, 5, "Quiltro", "pepito")
dog2 = Dog(13, 1, "Pitbull", "Juanito")
Dog.view_list()


class Phone:
    phone_list = []

    def __init__(self, marca, modelo, precio) -> None:
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        Phone.phone_list.append(self)

    def __str__(self) -> str:
        return f"Modelo:{self.modelo}, Marca: {self.marca}, Precio: {self.precio}"

    @classmethod
    def view_phones(cls):
        for phone in cls.phone_list:
            print(f"{phone}")


phone1 = Phone("Samsung", "A20", 10000)
phone2 = Phone("Apple", "Iphone 5", 200000)

Phone.view_phones()


class People(Phone):

    def __init__(self, marca, modelo, precio, nombre, sexo, rut) -> None:
        Phone.__init__(self, marca, modelo, precio)
        self.nombre = nombre
        self.sexo = sexo
        self.rut = rut
        # datos = []
        # datos.append(self)

    def mostrarDatos(self):
        print(self)

    def __str__(self) -> str:
        return super().__str__()


peopleFirst = People("samsung", "a20", 1000, "juanito", "binario", "19-12312")
peopleFirst.mostrarDatos()
print(peopleFirst)


class Pedido:
    def __init__(self, numero, productos):
        self.numero = numero
        self.productos = productos

    def __repr__(self):
        return f"Pedido(numero={self.numero}, productos={self.productos})"


doggis = Pedido(123, "hotdog")

print(doggis)


class RegistroVentas:
    def __init__(self) -> None:
        self.lista = []

    def agregarMonto(self, monto):
        self.lista.append(monto)

    def __len__(self):
        return len(self.lista)


venta1 = RegistroVentas()
print(len(venta1))
venta1.agregarMonto(123)
print(len(venta1))


class Leches:
    def __init__(self, marca, calorias, mls) -> None:
        self.marca = marca
        self.calorias = calorias
        self.mls = mls


class Productos:

    listaProductos = []

    def __init__(self, nombreProducto, precioProducto) -> None:
        self.cantidades = 0
        self.nombreProducto = nombreProducto
        self.precioProducto = precioProducto
        Productos.listaProductos.append(self)

    def restarCantidad(self, cantidad):
        self.cantidades -= (cantidad)

    def agregarCantidad(self, cantidad):
        self.cantidades += (cantidad)

    @classmethod
    def mostrarProductos(cls):
        contador = 1
        for p in cls.listaProductos:
            print(f"Producto Numero{contador}:{p}")
            contador += 1

    def __repr__(self) -> str:
        return f"Nombre:{self.nombreProducto} Precio:{self.precioProducto} Stock:{self.cantidades}"


producto1 = Productos("Leche", 100000)
print(producto1)
producto1.agregarCantidad(10000)
print(producto1)
producto1.restarCantidad(10000)
print(producto1)

producto2 = Productos("Chocolate", 200000)
print(producto2)
producto2.agregarCantidad(20000)
print(producto2)
producto2.restarCantidad(20000)
print(producto2)

Productos.mostrarProductos()


class CalculadoraFibonacci:
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result
        else:
            raise StopIteration


fibonacci_calculator = CalculadoraFibonacci(n=10)

for valor in fibonacci_calculator:
    print(valor)
