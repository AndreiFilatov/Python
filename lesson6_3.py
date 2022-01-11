class Worker:

    def __init__(self, name='Иван', surname='Иванов', position='Рядовой сотрудник', wage=500, bonus=1000):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage' : wage, 'bonus' : bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{12 * self._income["wage"] + self._income["bonus"]}')


print('-----> Объект Manager класса Position')
manager = Position('Илья', 'Обломов', 'Менеджер', 100, 100)
print('--> Атрибуты')
print(f'\tname: {manager.name}')
print(f'\tsurname: {manager.surname}')
print(f'\tposition: {manager.position}')
print(f'\t_income: {manager._income}')
print('--> Методы')
print('\tget_full_name: ', end='')
manager.get_full_name()
print('\tget_total_income: ', end='')
manager.get_total_income()
print()

print('-----> Объект General Director класса Position')
gen_dir = Position('Григорий', 'Печорин', 'Генеральный директор')
print('--> Атрибуты')
print(f'\tname: {gen_dir.name}')
print(f'\tsurname: {gen_dir.surname}')
print(f'\tposition: {gen_dir.position}')
print(f'\t_income: {gen_dir._income}')
print('--> Методы')
print('\tget_full_name: ', end='')
gen_dir.get_full_name()
print('\tget_total_income: ', end='')
gen_dir.get_total_income()
print()