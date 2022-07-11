from abc import ABC, abstractmethod
from typing import List


class Place(ABC):
    is_planet: bool

    @abstractmethod
    def get_antagonist(self):
        ...

    @abstractmethod
    def get_id(self):
        ...

    @property
    def address(self):
        return self.get_id(), self.is_planet


class City:
    is_planet: bool = False
    name: str

    def get_id(self):
        return f'{self.name}'


class Planet:
    is_planet: bool = True
    coordinates: List[float]

    def get_id(self):
        return f'{self.coordinates}'


class Kostroma(City, Place):
    name = 'Kostroma'

    @staticmethod
    def get_orcs():
        print('Orcs hid in the forest')

    def get_antagonist(self):
        self.get_orcs()


class Tokyo(City, Place):
    name = 'Tokyo'

    @staticmethod
    def get_godzilla():
        print('Godzilla stands near a skyscraper')

    def get_antagonist(self):
        self.get_godzilla()


