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
          self.bet=1
          self.win=None


class Dealer():
    def __init__(self):
        self.hand = Hand()

    def reset_hand(self):
        self.hand = Hand()

      def hit(self):
          self.add_card(self.shoe.draw_card())
          if self.reveal()>21:
              self.win=False
              return self.win
          self.win=True
          return self.win

      def stand(self):
          pass

      def resolve_bet(self,dealer):
          dealer_value=dealer.reveal()
          player_value=self.reveal()
          if player_value>21:
              self.win= False
          elif dealer_value>21:
               self.win = True
          elif player_value>dealer_value:
               self.win=True
          elif player_value== dealer_value:
               self.win= None
          else:
              self.win=False

          if self.win is True:
             self.hand_value +=self.bet*2
          elif self.win is None:
               self.hand_money+=self.bet

          if self.win is False:
             self.hand_value-=self.bet*2
             pass
          return self.win


    def show_initial_card(self):
        return str(self.hand.cards[0])

    def play(self, shoe):
        while self.hand.get_value() < 17:
            self.hand.add_card(shoe.deal_card())



class Game:
    def __init__(self):
        self.money = 0

    def play_a_round(self):
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()



        for i in range(2):
            player_hand.add_card(shoe.draw_card())
            dealer_hand.add_card(shoe.draw_card())


            print("New Round!")
            print("Dealer shows:", dealer_hand.cards_in_hand[0])
            print(f"Your hand: {player_hand}")

            # Player Turn
            while player_hand.hand_value > 21:
                choice = print("Would you like to Hit or Stand? ").lower()
                if choice == 'Hit':
                    player.hand.add_card(shoe.draw_card())
                    print("Your hand:", player_hand)
                    if player_hand.hand_value > 21:
                        print("Busted! You LOSE!")
                        self.money -=1
                        return
                elif choice == 'Stand':
                    break
                else:
                    print("Please type 'Hit' or 'Stand'")

            print("Dealer's Hand:", dealer_hand)
            while dealer_hand < 17:
                dealer_hand.add_card(shoe.draw_card())
                print("Dealer hits:", dealer_hand)

            player_value = player_hand.hand_value
            dealer_value = dealer_hand.hand_value

            print(f"Your total: {player_value} | Dealer Total: {dealer_value}")

            if dealer_value > 21 or player_value > dealer_value:
                print("You Win!")
                self.money += 1
            elif dealer_value < 21 or player_value < dealer_value:
                print("You Lose!")
                self.money -= 1
            else:
                print("It's a push (tie)")

    def view_balance(self):
        print(f"Current Balance: ${self.money:2f}")

def main():
    print("Welcome to Blackjack!")
    game = Game()

    while True:
        game.play_a_round()
        game.view_balance()
        again = input("Would you like to play again? (y/n): ").lower()
        if again != 'y':
            print(f"Thanks for playing! Final Balance is ${game.money}")
            break

if __name__ == "__main__":
    main()




        




