import random

SUITS = ["Diamonds", "Hearts". "Spades", "Clubs"]
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11


class Card:


    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    #repr function returns string representation
    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def _get_type_of_card(self, result):
        if result in self.cards:
            self.type_of_card = result
        return self.type_of_card

    def get_value_of_card(self, result):
        self.value_of_card = self._get_type_of_card(result)
        return self.value_of_card

class Deck:
    def __init__(self):
        self.cards =[]
        for suits in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))



class Shoe:
    def __init__(self, number_of_decks=6):
            self.number_of_decks = number_of_decks
            self.cards = []
            self.create_shoe()

    def create_shoe(self):
            self.cards = []
            for card in range(self.number_of_decks):
                deck = Deck()
                self.cards.extend(deck.cards)
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_a_card(self):
        if len(self.cards) < 100:
            print("Reshuffling the cards")
            self.create_shoe()
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_a_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.value == "A":
            self.aces += 1
        self.adjust_if_ace()

    def adjust_if_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def repr(self):
        return f"Hand({self.cards}), Value: {self.value} "

#Part 2


