from decimal import Decimal


class Fraction:

    def __init__(self, num, den):
        self.num = Decimal(str(num))
        self.den = Decimal(str(den))

    def to_decimal(self):
        return Decimal(self.num) / Decimal(self.den)

    def to_reduced_shape(self):
        gcd = self._gcd(self.num, self.den)
        reduced_num = self.num / gcd
        reduced_den = self.den / gcd
        return '{}/{}'.format(
            reduced_num,
            reduced_den
        )

    def _gcd(self, a, b):
        _a, _b = (a, b) if a > b else (b, a)
        if b == 0:
            return a
        return self._gcd(b, a % b)

    def product(self, that):
        num = self.num * that.num
        den = self.den * that.den
        return Fraction(num, den)

    def addition(self, that):
        num0 = self.den * that.num
        num1 = self.num * that.den
        den0 = self.den * that.den
        return Fraction(num0 + num1, den0)

    def __add__(self, that):
        return self.addition(that)

    def __mul__(self, that):
        return self.product(that)

    def __str__(self):
        return '{}/{}'.format(
            self.num,
            self.den
        )

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return id(self)

    def __lt__(self, that):
        return True if self.to_decimal() < that.to_decimal() else False

    def __gt__(self, that):
        return not self.__lt__(that)



_f0 = Fraction(3, 6)
_f1 = Fraction(4, 8)

lista = [
    Fraction(3, 6),
    Fraction(6, 6),
    Fraction(9, 6),
    Fraction(25, 8),
    Fraction(3, 4),
    Fraction(1, 6),
    Fraction(7, 6),
    Fraction(11, 6),
    Fraction(26, 11),
    Fraction(33, 8),
]
lista.sort()

print(lista)

conjunto = set()
conjunto.add(_f0)
conjunto.add(_f1)

print(conjunto)
print(_f0 + _f1)
print(_f0 * _f1)

