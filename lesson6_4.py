class Car:

    def __init__(self, speed=0, color='unknown', name='unnamed', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала.')

    def stop(self):
        print(f'Машина {self.name} остановилась.')

    def turn(self, direction=''):
        if direction == 'left':
            print(f'Машина {self.name} повернула налево.')
        elif direction == 'right':
            print(f'Машина {self.name} повернула направо.')
        else:
            print(f'У машины {self.name} неизвестное направление.')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')


class TownCar(Car):
    type_car = 'TownCar'

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости: скорость свыше 60 !')
        else:
            Car.show_speed(self)


class SportCar(Car):
    type_car = 'SportCar'


class WorkCar(Car):
    type_car = 'WorkCar'

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости: скорость свыше 40 !')
        else:
            Car.show_speed(self)


class PoliceCar(Car):
    type_car = 'PoliceCar'

    def __init__(self, speed=0, color='unknown', name='unnamed', is_police=True):
        super().__init__(speed, color, name, is_police)


print('-----> Объект класса TownCar')
tc = TownCar(0, 'silver', 'Mazda')
print('--> Атрибуты')
print(f'\tspeed: {tc.speed}')
print(f'\tcolor: {tc.color}')
print(f'\tname: {tc.name}')
print(f'\tis_police: {tc.is_police}')
print(f'\ttype_car: {tc.type_car}')
print('--> Методы')
print('\tgo: ', end='')
tc.go()
tc.speed = 50
print('\tturn: ', end='')
tc.turn('left')
print('\tturn: ', end='')
tc.turn()
print('\tturn: ', end='')
tc.turn('right')
print('\tshow_speed: ', end='')
tc.show_speed()
tc.speed = 80
print('\tshow_speed: ', end='')
tc.show_speed()
print()


print('-----> Объект класса SportCar')
sc = SportCar(100, 'red', 'Ferrari')
print('--> Атрибуты')
print(f'\tspeed: {sc.speed}')
print(f'\tcolor: {sc.color}')
print(f'\tname: {sc.name}')
print(f'\tis_police: {sc.is_police}')
print(f'\ttype_car: {sc.type_car}')
print('--> Методы')
print('\tturn: ', end='')
sc.turn()
print('\tturn: ', end='')
sc.turn('right')
print('\tshow_speed: ', end='')
sc.show_speed()
sc.speed = 30
print('\tshow_speed: ', end='')
sc.show_speed()
print('\tstop: ', end='')
sc.stop()
print()


print('-----> Объект класса WorkCar')
wc = WorkCar(10, 'black', 'Mercedes-Benz')
print('--> Атрибуты')
print(f'\tspeed: {wc.speed}')
print(f'\tcolor: {wc.color}')
print(f'\tname: {wc.name}')
print(f'\tis_police: {wc.is_police}')
print(f'\ttype_car: {wc.type_car}')
print('--> Методы')
print('\tturn: ', end='')
wc.turn('right')
print('\tturn: ', end='')
wc.turn('left')
print('\tshow_speed: ', end='')
wc.show_speed()
wc.speed = 120
print('\tshow_speed: ', end='')
wc.show_speed()
print('\tstop: ', end='')
wc.stop()
print()


print('-----> Объект класса PoliceCar')
pc = PoliceCar(color='black', name='Priora')
print('--> Атрибуты')
print(f'\tspeed: {pc.speed}')
print(f'\tcolor: {pc.color}')
print(f'\tname: {pc.name}')
print(f'\tis_police: {pc.is_police}')
print(f'\ttype_car: {pc.type_car}')
print('--> Методы')
print('\tgo: ', end='')
pc.go()
pc.speed = 200
print('\tturn: ', end='')
pc.turn()
print('\tturn: ', end='')
pc.turn('left')
print('\tshow_speed: ', end='')
pc.show_speed()
pc.speed = 20
print('\tshow_speed: ', end='')
pc.show_speed()
print('\tstop: ', end='')
pc.stop()
print()