import random


class Card:

    cards = {"Jack": 10, "King": 10, "Queen": 10,
             "10": 10, "9": 9, "8": 8, "7": 7, "6": 6,
             "5": 5, "4": 4, "3": 3, "2": 2, "Ace": 1}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value_of_card = 0
        self.type_of_card = ""

    def _get_type_of_card(self, result):
        if result in self.cards:
            self.type_of_card = result
        return self.type_of_card

    def get_value_of_card(self, result):
        self.value_of_card = self._get_type_of_card(result)
        return self.value_of_card

class Shoe:
    def __init__(self, number_of_decks = 6):
        self.number_of_decks = number_of_decks
        self.cards = []
        self.create_shoe()

    def create_shoe(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "Q", "K"]
        suits = ["♠️", "♦️", "❤️", "♣️"]
        self.cards = []
        for deck in range(self.number_of_decks):
            for rank in ranks:
                for suit in suits:
                    self.cards.append(Card(rank,suit))


