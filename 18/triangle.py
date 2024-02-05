import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = bp = self.a + self.b + self.c
        self.c = c


    def __init__(self):
        self.a = int(input())
        self.b = int(input())
        self.c = int(input())
    def per(self):
        p = self.a + self.b + self.c
        return p

    def square(self):
        p = self.per() / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return s

    def alpha(self):
        return math.asin(self.b/self.c)*180/math.pi
    def betta(self):
        return math.asin(self.a/self.c)*180/math.pi
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c
tr1 = Triangle()
tr2 = Triangle()
print(tr1.per())
print(tr1.square())
print(tr1.alpha())
print(tr1.betta())
print(tr1 == tr2)