from typing import Union
from heroes import Superman, SuperHero, ChackNorris
from places import Kostroma, Tokyo
from massmedia import MassMedia


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo], mass_media: MassMedia):
    hero.find(place)
    hero.attack()
    mass_media.create_news(hero, place)


if __name__ == '__main__':
    media = MassMedia([('Vologda', False), ([2.4511, 0.1881455], True)])
    save_the_place(Superman(), Kostroma(), media)
    print('-' * 20)
    save_the_place(ChackNorris(), Tokyo(), media)