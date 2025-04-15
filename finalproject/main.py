import random

class Card:
    cards = {"Jack": 10, "King": 10, "Queen": 10,
             "10": 10, "9": 9, "8": 8, "7": 7, "6": 6,
             "5": 5, "4": 4, "3": 3, "2": 2, "Ace": 1}

    def __init__(self):
        self.value_of_card = 0
        self.type_of_card = ""

    def _get_type_of_card(self, result):
        if result in self.cards:
            self.type_of_card = result
        return self.type_of_card

    def get_value_of_card(self, result):
        self.value_of_card = self._get_type_of_card(result)
        return self.value_of_card

class Deck:
      def __int__(self):
          self.deck=[]

      def make_deck(self):
          card=Card()
          card.type_of_card=random.randint(1,10)
          for i in range(1,53):
              self.deck.append(card)

class Shoe:

    def __init__(self):
            self.number_of_decks = 6
            self.shoe = []
            self.card_count=0

    def create_shoe(self):
        deck=Deck()
        for i in range(self.number_of_decks):
            deck.make_deck()
            self.shoe.append(deck)

    def shuffle(self):
        for j_deck in enumerate(self.shoe):
            self.card_count+=len(self.shoe[j_deck])
        if self.card_count<100:
           self.create_shoe()

class Hand:

      def __init__(self):
          self.number_of_cards=2
          self.cards_in_hand=[]
          self.hand_value=0

      def __len__(self):
          return len(self.cards_in_hand)

      def check_valid_hand(self):
          return len(self.cards_in_hand)>0

      def give_cards_to_hand(self):
          shoe=Shoe()
          shoe.create_shoe()
          random_deck=random.randint(1,7)
          random_card=random.randint(1,53)
          if not self.check_valid_hand():
             for i in range(1,3):
                 self.cards_in_hand.append(shoe.shoe[random_deck][random_card])
          return self.cards_in_hand






















