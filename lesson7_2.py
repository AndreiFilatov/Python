from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def fabric_exp(self):
        pass


class Coat(Clothes): # Пальто

    def __init__(self, size=0):
        if not isinstance(size, (int,float)) or size < 0:
            self.size = 0
        else:
            self.size = size

    def fabric_exp(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes): # Костюм

    def __init__(self, growth=0):
        if not isinstance(growth, (int,float)) or growth < 0:
            self.growth = 0
        else:
            self.growth = growth

    @property
    def fabric_exp(self):
        return 2 * self.growth + 0.3

ct = Coat(54)
print(f'Раcход ткани на пальто: {ct.fabric_exp():.2f}')

st = Suit(181)
print(f'Раcход ткани на костюм: {st.fabric_exp:.2f}')