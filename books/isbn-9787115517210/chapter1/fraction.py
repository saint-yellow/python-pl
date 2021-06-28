class Fraction(object):
    def __init__(self, top, buttom):
        self.numerator = top
        self.denumerator = buttom

    def get_numerator(self):
        return self.numerator

    def get_denumerator(self):
        return self.denumerator

    @staticmethod
    def _gcd(m: int, n: int) -> int:
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n

    def __add__(self, other):
        new_numerator = self.numerator * other.denumerator + self.denumerator * other.numerator
        new_denumerator = self.denumerator * other.denumerator
        common_divisor = Fraction._gcd(new_numerator, new_denumerator)
        return Fraction(new_numerator // common_divisor, new_denumerator // common_divisor)

    def __repr__(self):
        return str(self.numerator) + "/" + str(self.denumerator)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass
