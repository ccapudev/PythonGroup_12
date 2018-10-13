class Calc:

    version = '1.0'  # atributo global

    def __init__(self, name):
        self.name = name

    def model(self):
        return self.name

    @staticmethod
    def sum(x, y):
        return x + y


# calc = Calc('ejemplo')
# print(calc.sum(2, 3))
# Un método estático puede llamarse desde la clase
print(Calc.sum(2, 3))

# Un atributo global es el mismo para todos los objetos
print(Calc.version)
calc3 = Calc('CasioT59')
Calc.version = '3.0'
calc = Calc('CasioT60')
calc2 = Calc('CasioT61')
print(calc.version)
print(calc2.version)
print(calc3.version)

# Podemos agregar atributos después de creado el objeto
print(dir(calc))
calc.serie = '404'
print(dir(calc))

