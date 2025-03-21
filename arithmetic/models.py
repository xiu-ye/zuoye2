from fractions import Fraction


class Number:
    def __init__(self, value):
        if isinstance(value, int):
            self.num = value
            self.den = 1
        elif isinstance(value, Fraction):
            self.num = value.numerator
            self.den = value.denominator
        else:
            parts = str(value).split('/')
            if "'" in parts[0]:
                whole, frac = parts[0].split("'")
                whole = int(whole)
                self.num = whole * int(frac.split('/')[1]) + int(frac.split('/')[0])
                self.den = int(frac.split('/')[1])
            else:
                self.num = int(parts[0])
                self.den = int(parts[1]) if len(parts) > 1 else 1

    def simplify(self):
        from .utils import gcd
        g = gcd(self.num, self.den)
        return Number(Fraction(self.num // g, self.den // g))

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        if self.num > self.den:
            whole = self.num // self.den
            remainder = self.num % self.den
            return f"{whole}'{remainder}/{self.den}"
        return f"{self.num}/{self.den}"

    def to_fraction(self):
        return Fraction(self.num, self.den)


class ExpressionNode:
    def __init__(self, left=None, op=None, right=None, value=None):
        self.left = left
        self.op = op
        self.right = right
        self.value = value

    def is_leaf(self):
        return self.left is None and self.right is None