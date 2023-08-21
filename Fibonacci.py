class CalcularFibonacci:

    def __init__(self, n) -> None:
        self.primero = 0
        self.segundo = 1
        self.cantidad = n
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.contador < self.cantidad:
            numeroActual = self.primero
            self.primero, self.segundo = self.segundo, self.primero + self.segundo
            self.contador += 1
            return numeroActual
        else:
            raise StopIteration


primerValor = CalcularFibonacci(5)

for N in primerValor:
    print(N)
