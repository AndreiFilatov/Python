import time

class TrafficLight:
    __color = None

    def running(self):
        print('Светофор включен.')

        # Состояние: красный
        self.__color = 'КРАСНЫЙ'
        print(f'\tСвет светофора: {self.__color}')
        print('\t\tПереключение через:')
        for i in range(1, 8).__reversed__():
            print(f'\t\t\t{i}...')
            time.sleep(1)

        # Состояние: желтый
        self.__color = 'ЖЕЛТЫЙ'
        print(f'\tСвет светофора: {self.__color}')
        print('\t\tПереключение через:')
        for i in range(1, 3).__reversed__():
            print(f'\t\t\t{i}...')
            time.sleep(1)

        # Состояние: зеленый
        self.__color = 'ЗЕЛЕНЫЙ'
        print(f'\tСвет светофора: {self.__color}')
        print('\t\tВыключение через:')
        for i in range(1, 10).__reversed__():
            print(f'\t\t\t{i}...')
            time.sleep(1)

        # Состояние: выключен
        print('Светофор выключен.')
        self.__color = None

semaphore = TrafficLight()
semaphore.running()