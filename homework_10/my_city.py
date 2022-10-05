import random
from typing import List


class Street:
    def __init__(self, number):
        self.number = number
        self.houses = []

    def add_house(self):
        self.houses.append(House(len(self.houses) + 1))

    def remove_house(self, house_number):
        self.houses.pop(house_number - 1)

    def create_houses_in_the_street(self):
        self.houses = list(range(1, random.randint(5, 20)))
        return self.houses


class House:
    def __init__(self, number):
        self.population = 0
        self.number = number

    def add_population(self):
        self.population = random.randint(1, 100)


class City:
    def __init__(self, name: str):
        self.name = name
        self.population = 0
        self.streets: List[Street] = list()
        self.houses: List[House] = list()

    def add_street(self):
        self.streets.append(Street(len(self.streets) + 1))

    def delete_street(self, street_number):
        self.streets.pop(street_number - 1)

    def get_population(self) -> int:
        all_population = len(self.streets) * len(self.houses) * self.population
        return all_population

    def fill_the_city(self):
        self.streets = list(range(1, random.randint(1, 10)))
        self.houses = list(range(1, random.randint(5, 20)))
        self.population = random.randint(1, 100)
        return self.streets, self.houses, self.population

    def the_city_in_table(self):
        all_city = ['Street', 'House', 'Population'], \
                   [str(elem) for elem in self.streets], \
                   [str(elem) for elem in self.houses], \
                   [str(elem) for elem in self.population]
        print('    '.join(all_city[0]))
        iterate_data = iter(all_city)
        next(iterate_data)
        for row in iterate_data:
            print(' '.join([elem.ljust(8) for elem in row]))


if __name__ == '__main__':
    pass


