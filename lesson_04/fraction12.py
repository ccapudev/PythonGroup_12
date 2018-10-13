class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def to_decimal(self):
        return self.num / self.den

    def to_reduced_shape(self):
        gcd = self._gcd(self.num, self.den)
        reduced_num = self.num / gcd
        reduced_den = self.den / gcd
        return '{:.0f} / {:.0f}'.format(reduced_num, reduced_den)

    def _gcd(self, a, b):
        if b == 0:
            return a
        return self._gcd(b, a % b)

    def product(self, that):
        num = self.num * that.num
        den = self.den * that.den
        return Fraction(num, den)

    def __mul__(self, that):
        return self.product(that)

    def addition(self, that):
        num = self.num * that.den + that.num * self.den
        den = self.den * that.den
        return Fraction(num, den)

    def __add__(self, that):
        return self.addition(that)

    def __lt__(self, that):
        if self.to_decimal() < that.to_decimal():
            return True
        return False

    def __str__(self):
        return '{} / {}'.format(self.num, self.den)

    def __repr__(self):
        return '{} / {}'.format(self.num, self.den)


# 2 / 3 * 1 / 2 = 2 / 6
fraction = Fraction(2, 3)
fraction2 = Fraction(1, 2)
# print(fraction.to_decimal())
# print(fraction.to_reduced_shape())
# No hacer print(fraction._gcd(18, 21))
# fraction3 = fraction.product(fraction2)
fraction3 = fraction * fraction2
# print(fraction3.to_reduced_shape())

# fraction4 = fraction.addition(fraction2)
fraction4 = fraction + fraction2
# print(fraction4.to_reduced_shape())

list_fraction = [fraction, fraction2, fraction3, fraction4]
print(fraction)
print(list_fraction)
list_fraction.sort()
print(list_fraction)
