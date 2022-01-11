class Stationery:
    title = 'Unknown stationery'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self):
        self.title = 'Pen'

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):

    def __init__(self):
        self.title = 'Pencil'

    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):

    def __init__(self):
        self.title = 'Handle'

    def draw(self):
        print('Запуск отрисовки маркером')


print('-----> Объект класса Stationery')
print('--> До определения объекта:')
print(f'\tАтрибут title: {Stationery.title}')
print('--> После определения объекта:')
sr = Stationery()
print(f'\tАтрибут title: {sr.title}')
print(f'\tМетод draw: ', end='')
sr.draw()
print()

print('-----> Объект класса Pen')
print('--> До определения объекта:')
print(f'\tАтрибут title: {Pen.title}')
print('--> После определения объекта:')
pn = Pen()
print(f'\tАтрибут title: {pn.title}')
print(f'\tМетод draw: ', end='')
pn.draw()
print()

print('-----> Объект класса Pencil')
print('--> До определения объекта:')
print(f'\tАтрибут title: {Pencil.title}')
print('--> После определения объекта:')
pl = Pencil()
print(f'\tАтрибут title: {pl.title}')
print(f'\tМетод draw: ', end='')
pl.draw()
print()

print('-----> Объект класса Handle')
print('--> До определения объекта:')
print(f'\tАтрибут title: {Handle.title}')
print('--> После определения объекта:')
hl = Handle()
print(f'\tАтрибут title: {hl.title}')
print(f'\tМетод draw: ', end='')
hl.draw()
print()
