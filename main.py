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


class Deck:
    def __init__(self, number_of_jokers=0, composition=None):
        self.number_of_jokers = number_of_jokers
        self.composition = composition

        if composition is None:
            self.composition = make_deck(self.number_of_jokers)

    def draw(self, number_of_cards=1):
        cards = random.choices(self.composition, k=number_of_cards)

        for card in cards:
            self.composition.remove(card)

        if number_of_cards == 1:
            return cards[0]
        else:
            return cards

    def get_composition(self):
        return self.composition


def make_deck(jokers=0):
    deck = []
    for suit in ["S", "D", "C", "H"]:
        deck.append(f"A{suit}")
        for number in range(2, 10):
            deck.append(f"{number}{suit}")
        for face in ["T", "J", "Q", "K"]:
            deck.append(f"{face}{suit}")

    for number in range(jokers):
        deck.append(f"J{number}")

    return deck
