class Matrix:

    def __init__(self, matrix=''):
        self.n_row = len(matrix) # число строк матрицы
        if not isinstance(matrix, list): # если входные данные не являются списком,
            self.reset() # то считаем матрицу неопределенной
        elif self.n_row == 0: # если входной список пустой,
            self.reset() # то считаем матрицу неопределенной
        else:
            self.n_col = len(matrix[0]) # число столбцов матрицы
            for l in matrix[1:]:
                if self.n_col != len(l): # если число элементов внутри вложенных списков различно,
                    self.reset() # то считаем матрицу неопределенной
                    return
                for el in l:
                    if not isinstance(el, (int, float)): # если отдельные элементы не являются числовыми,
                        self.reset() # то считаем матрицу неопределенной
                        return
            self.matrix = matrix

    def reset(self): # сброс атрибутов
        self.n_row = None
        self.n_col = None
        self.matrix = None

    def __str__(self):
        if self.matrix:
            out = f'{self.__class__.__name__} {self.n_row} x {self.n_col}:\n\t'
            for row in self.matrix:
                out += ' '.join([str(el) for el in row]) + '\n\t'
            out = out[:len(out)-1]
        else:
            out = 'Матрица не определена'
        return out

    def __add__(self, other):
        if self.n_row != other.n_row or self.n_col != other.n_col:
            matrix = ''
        else:
            matrix =[]
            for i in range(self.n_row):
                matrix.append([self.matrix[i][j] + other.matrix[i][j] for j in range(self.n_col)])
        return Matrix(matrix)



A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)

B = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(B)

C = A + B
print(C)