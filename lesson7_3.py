class Cell:

    def __init__(self, n=0):
        if not isinstance(n, int) or n <= 0:
            self.n_box = None
        else:
            self.n_box = n

    def __add__(self, other):
        return Cell(self.n_box + other.n_box)

    def __sub__(self, other):
        diff = max(0, self.n_box - other.n_box)
        if diff == 0:
            print('\tВычитание клеток произвести не удалось!')
        return Cell(diff)

    def __mul__(self, other):
        return Cell(self.n_box * other.n_box)

    def __truediv__(self, other):
        return Cell(self.n_box // other.n_box)

    def make_order(self, len_row=1):
        if len_row < 0:
            len_row = 1
        else:
            n_row = self.n_box // len_row + 1
            res = ''
            for i in range(1,n_row):
                res += '*' * len_row + '\\n'
            res += '*' * (self.n_box % len_row)
        return res



print('Исходные клетки')
a = Cell(9)
print(f'\tЧисло ячеек клетки а: {a.n_box}')

b = Cell(5)
print(f'\tЧисло ячеек клетки b: {a.n_box}')

print()

print('Сложение клеток')
c = a + b
print(f'\tЧисло ячеек клетки c = a + b: {c.n_box}')

print()

print('Вычитание клеток')
c = a - b
print(f'\tЧисло ячеек клетки c = a - b: {c.n_box}')
c = b - a
print(f'\tЧисло ячеек клетки c = b - a: {c.n_box}')

print()

print('Умножение клеток')
c = a * b
print(f'\tЧисло ячеек клетки c = a * b: {c.n_box}')

print()

print('Деление клеток')
c = a / b
print(f'\tЧисло ячеек клетки c = a / b: {c.n_box}')
c = b / a
print(f'\tЧисло ячеек клетки c = b / a: {c.n_box}')

print()

print('Организация ячеек по рядам')
print(f'\tРезультат для ячейки a: {a.make_order(5)}')
print(f'\tРезультат для ячейки b: {b.make_order(10)}')