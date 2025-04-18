import random

class Card:
    cards = {"Jack": 10, "King": 10, "Queen": 10,
             "10": 10, "9": 9, "8": 8, "7": 7, "6": 6,
             "5": 5, "4": 4, "3": 3, "2": 2, "Ace": 1}

    def __init__(self,type_of_card):
        self.value_of_card = 0
        self.type_of_card = self.cards[type_of_card]

    def get_value_of_card(self):
        return self.value_of_card

    def __str__(self):
        return self.type_of_card

class Deck:
      def __init__(self):
          self.deck=[]

      def make_deck(self):
          ranks=list(Card.cards.keys())
          suits=["Hearts","Diamonds","Clubs","Spades"]
          for suit in suits:
              for rank in ranks:
                  self.deck.append(Card(suit))

class Shoe:

    def __init__(self):
            self.number_of_decks = 6
            self.shoe = []
            self.card_count=0
            self.create_shoe()

    def create_shoe(self):
        self.shoe=[]
        for i in range(self.number_of_decks):
            deck=Deck()
            deck.make_deck()
            self.shoe.extend(deck.deck)
        self.card_count=len(self.shoe)
        self.shuffle()

    def shuffle(self):
        if self.card_count < 100:
            self.create_shoe()
        random.shuffle(self.shoe)
        self.card_count = len(self.shoe)


    def draw_card(self):
        if not self.shoe:
            self.create_shoe()
        self.card_count-=1
        return self.shoe.pop()

class Hand:

      def __init__(self,shoe):
          self.shoe=shoe
          self.cards_in_hand=[]
          self.hand_value=0
          self.ace_count=0

      def __len__(self):
          return len(self.cards_in_hand)

      def check_valid_hand(self):
          return len(self.cards_in_hand)>0

      def add_card(self,new_card):
          self.cards_in_hand.append(new_card)
          if new_card.type_of_card=="Ace":
             self.ace_count+=1
          self.hand_value+=new_card.get_value_of_card()
          temp_value=self.hand_value
          temp_aces=self.ace_count
          while temp_value>21 and temp_aces>0:
                temp_value-=10
                temp_aces-=1
          self.hand_value=temp_value

      def reveal(self):
          return self.hand_value

      def deal_initial_cards(self):
          if not self.check_valid_hand():
             for i in range(2):
                 self.add_card(self.shoe.draw_card())

class Player(Hand):

      def __init__(self,shoe):
          super().__init__(shoe)
          self.hand_money=1
          self.bet=0
          self.win=None

class Dealer():
    def __init__(self):
        self.hand = Hand()

    def reset_hand(self):
        self.hand = Hand()

    def show_initial_card(self):
        return str(self.hand.cards[0])

    def play(self, shoe):
        while self.hand.get_value() < 17:
            self.hand.add_card(shoe.deal_card())



def main():
    shoe = Shoe()
    player = Player()
    dealer = Dealer()
    balance = 1

    while True:
        if len(shoe.cards) < 100:
            print("Reshuffling the shoe")
            shoe.shuffle()


        player.hand_reset()
        dealer.hand_reset()

        for i in range(2):
            player.hand.deal_initial_cards(shoe)
            dealer.hand.deal_initial_cards(shoe)

            print("New Round!")
            print("Dealer shows: ")
            print(f"Your hand: {player.hand}")

            # Player Turn
            while player.hand_value > 21:
                choice = print("Would you like to Hit or Stand? ").strip().lower()
                if choice == 'Hit':
                    player.hand.add_card(shoe.draw_card())
                elif choice == 'Stand':
                    break
                else:
                    print("Please type 'Hit' or 'Stand'")

        if player.hand_value > 21:
            print("Busted! You lost $1")
            balance -= 1

        #Player's Turn
        else:
            dealer.hand





