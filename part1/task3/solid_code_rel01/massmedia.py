from typing import List
from places import Place


class MassMedia:
    def __init__(self, subscribers_list: List[tuple] = None):
        self.subscribers_list = []
        if subscribers_list:
            self.get_subscribe_addresses(subscribers_list)

    def get_subscribe_addresses(self, subscribers_list: List[tuple]):
        for item in subscribers_list:
            self.subscribe(item)

    @staticmethod
    def get_address(place_id: List[float] or str, planet: bool):
        if planet:
            address = f'On planet with coordinates {place_id}'
        else:
            address = f'In city {place_id}'
        return address

    def subscribe(self, place: tuple):
        address = self.get_address(*place)
        if address not in self.subscribers_list:
            self.subscribers_list.append(address)

    @staticmethod
    def get_article(hero, place: Place):
        hero_name = getattr(hero, 'name', 'hero')
        place_name = getattr(place, 'name', 'place')
        return f'{hero_name} saved the {place_name}!'

    def create_news(self, hero, place: Place):
        news_article = self.get_article(hero, place)
        self.subscribe(place.address)
        for address in self.subscribers_list:
            print(f'{address} the news came out: {news_article}')
