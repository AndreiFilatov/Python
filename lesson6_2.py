class Road():

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, mass_unit, gage_unit):
        print(self._length * self._width * mass_unit * gage_unit)

way = Road(20, 5000)
way.calc_mass(mass_unit=25, gage_unit=5)