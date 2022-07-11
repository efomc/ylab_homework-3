from antagonistfinder import AntagonistFinder
from abc import ABC, abstractmethod


class SuperHero(ABC):
    def __init__(self, name):
        self.name = name
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    @abstractmethod
    def attack(self):
        ...


class GunShooter:
    def fire_a_gun(self):
        print('PIU PIU')


class RoundHouseKick:
    def roundhouse_kick(self):
        print('Bump')


class LasersIncinerate:
    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')


class ChackNorris(GunShooter, RoundHouseKick, SuperHero):
    def __init__(self):
        super(ChackNorris, self).__init__('Chack Norris')

    def attack(self):
        self.fire_a_gun()


class Superman(LasersIncinerate, SuperHero):
    def __init__(self):
        super(Superman, self).__init__('Clark Kent')

    def attack(self):
        self.incinerate_with_lasers()






