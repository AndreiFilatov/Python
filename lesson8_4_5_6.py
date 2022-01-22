from abc import ABC, abstractmethod


class Warehouse:
    """
    Класс Склад Оргтехники
    dict - словарь: ключ - тип техники, значение - словарь из конкретных объектов
    capacity - максимальный объем склада (максимальное кол-во объектов)
    fill_count - заполненность склада (текущее кол-во объектов на складе)
    free_id - текущий свободный уникальный номер объекта в рамках склада
    """

    def __init__(self):
        self.__capacity = 1000
        self.__fill_count = 0
        self.__free_id = 1
        self.__dct = {'Printer' : {}, 'Scanner' : {}, 'Xerox' : {}}

    def append(self, obj, department):
        if self.__fill_count + 1 > self.__capacity:
            print('Добавление объекта на склад невозможно, склад переполнен !')
        else:
            self.__fill_count += 1
            obj.id = self.get_id
            self.__free_id += 1
            self.__dct[obj.__class__.__name__][obj.id] = {'Отдел' : department,
                                                          'Характеристики' : obj.get_characteristics_list}

    @property
    def get_id(self):
        return self.__free_id

    @property
    def get_all_objects(self):
        if self.__fill_count > 0:
            print('-----------------------> СКЛАД <-----------------------')
            print_dict = {'Printer' : 'принтеры', 'Scanner' : 'сканеры', 'Xerox' : 'ксероксы'}
            for key, value in self.__dct.items():
                l = len(value)
                print(f'---> {print_dict[key].upper()} (кол-во - {l})')
                if l > 0:
                    for key_obj, value_obj in value.items():
                        print(f'\t\tid = {key_obj}:')
                        for key, value in value_obj.items():
                            print(f'\t\t\t{key} : {value}')
        else:
            print('Склад пуст.')


class Office_Machines(ABC):
    """
    Класс Оргтехники
    id - уникальный номер объекта в рамках склада (присваивается в момент добавления объекта на склад)
    weight - вес объекта в кг: 2.5, 6
    """
    id = None
    weight = None

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_characteristics_list(self):
        pass


class Printer(Office_Machines):
    """
    Класс Принтер
    print_tech - технолология печати: лазерная, струйная, светодиодная
    print_speed - скорость печати: кол-во страниц в минуту
    print_color - возможность цветной печати: True, False
    """

    def __init__(self, weight=None, print_tech=None, print_speed=None, print_color=None):
        if weight:
            try:
                self.weight = float(weight)
            except ValueError:
                print('Вес принтера указан некорректно !')
        self.print_tech = str(print_tech)
        if print_speed:
            try:
                self.print_speed = int(print_speed)
            except ValueError:
                print('Скорость печати принтера указана некорректно !')
        self.print_color = print_color

    @property
    def get_characteristics_list(self):
        return [self.weight, self.print_tech, self.print_speed, self.print_color]


class Scanner(Office_Machines):
    """
    Класс Сканер
    scan_type - тип сканера: планшетный, протяжный
    scan_contoller - тип датчика: CIS, CCD
    scan_dimension - разрешение: 600 х 1200
    """

    def __init__(self, weight=None, scan_type=None, scan_contoller=None, scan_dimension=None):
        if weight:
            try:
                self.weight = float(weight)
            except ValueError:
                print('Вес сканера указан некорректно !')
        self.scan_type = str(scan_type)
        self.scan_contoller = str(scan_contoller)
        self.scan_dimension = str(scan_dimension)


    @property
    def get_characteristics_list(self):
        return [self.weight, self.scan_type, self.scan_contoller, self.scan_dimension]


class Xerox(Office_Machines):
    """
    Класс Ксерокс
    xer_func - набор функций: сканирование, копирование, распечатка
    xer_colors - количество цветов: 256
    xer_size - габариты: 400 x 300 x 300 мм
    """

    def __init__(self, weight=None, xer_func=None, xer_colors=None, xer_size=None):
        if weight:
            try:
                self.weight = float(weight)
            except ValueError:
                print('Вес ксерокса указан некорректно !')
        self.xer_func = str(xer_func)
        if xer_colors:
            try:
                self.xer_colors = int(xer_colors)
            except ValueError:
                print('Количество цветов ксерокса указано некорректно !')
        self.xer_size = str(xer_size)

    @property
    def get_characteristics_list(self):
        return [self.weight, self.xer_func, self.xer_colors, self.xer_size]


wh = Warehouse()

pr1 = Printer(2, 'Лазерная', 40, True)
pr2 = Printer(5, 'Струйная', 15, False)
sc1 = Scanner(10, 'Планшетный', 'CCD', '600 х 480')
xr1 = Xerox(15, 'Cканирование, копирование, распечатка', '2000', '400 x 300 x 300 мм')
xr2 = Xerox(30, 'Копирование', 16, '400 x 300 x 300 мм')

wh.append(pr1, 'IT')
wh.append(pr2, 'Продажи')
wh.append(sc1, 'Финансы')
wh.append(xr1, 'Бухгалтерия')
wh.append(xr1, 'Аналитики')

wh.get_all_objects