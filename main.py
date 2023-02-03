import random


class Dice:

    def __init__(self, sides=6, population=None, weights=None):
        self.sides = sides
        self.population = population
        self.weights = weights

        if population is None:
            self.population = list(range(1, self.sides))

    def roll(self):
        value = random.choices(self.population, self.weights)
        return value[0]

    def roll_series(self, rolls):
        values = random.choices(self.population, self.weights, k=rolls)
        return values
