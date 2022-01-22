class Complex:

    def __init__(self, a=0, b=0):
        try:
            self.a = float(a)
        except ValueError:
            self.a = 0
        try:
            self.b = float(b)
        except ValueError:
            self.b = 0

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    @property
    def record(self):
        return f'{self.a} + {self.b} * i'

print('Исходные комплексные числа')
a = Complex(2, 5)
print(f'\tЧисло а: {a.record}')

b = Complex(3, 7)
print(f'\tЧисло b: {b.record}')

print()

print('Сложение комплексных чисел')
c = a + b
print(f'\tЧисло c = a + b: {c.record}')

print()

print('Умножение комплексных чисел')
c = a * b
print(f'\tЧисло c = a * b: {c.record}')