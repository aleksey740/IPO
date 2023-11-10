import math
class Drob(object):
    """Дробь вида a/b"""
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.normalize()

    def __str__(self):
        return f'{self.a}/{self.b}'

    def __eq__(self, other):
        """Проверка на равенство"""
        return self.a * other.b == other.a * self.b

    def __lt__(self, other):
        """Проверка на меньше"""
        return self.a * other.b < other.a * self.b

    def __add__(self, other):
        """Сложение"""
        a1 = self.a * other.b + other.a * self.b
        b1 = self.b * other.b
        return Drob(a1, b1)

    def __sub__(self, other):
        """Вычитание"""
        a1 = self.a * other.b - other.a * self.b
        b1 = self.b * other.b
        return Drob(a1, b1)

    def __mul__(self, other):
        """Умножение"""
        a1 = self.a * other.a
        b1 = self.b * other.b
        return Drob(a1, b1)

    def __truediv__(self, other):
        """Деление"""
        a1 = self.a * other.b
        b1 = self.b * other.a
        return Drob(a1, b1)

    def normalize(self):
        """Приводит дробь вида 4/6 к 2/3"""
        c = math.gcd(self.a, self.b)
        self.a = self.a // c
        self.b = self.b // c

d1 = Drob(1,3)
d2 = Drob(2,5)
#Проверка
print(f'{d1} = {d2} {d1==d2}')
print(f'{d1} < {d2} {d1<d2}')

print(f'{d1} + {d2} = {d1 + d2}') #Сложение
print(f'{d1} - {d2} = {d1-d2}') #Вычитание
print(f'{d1} * {d2} = {d1*d2}') #Умножение
print(f'{d1} / {d2} = {d1/d2}') #Деление
