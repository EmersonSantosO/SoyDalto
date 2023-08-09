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
