import random
from random import choice


class Card:
    cards = {"Jack": 10, "King": 10, "Queen": 10,
             "10": 10, "9": 9, "8": 8, "7": 7, "6": 6,
             "5": 5, "4": 4, "3": 3, "2": 2, "Ace": 11}

    def __init__(self,type_of_card):
        self.value_of_card = self.cards[type_of_card]
        self.type_of_card = type_of_card

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
                  self.deck.append(Card(rank))

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

      def place_bet(self):
          if 1 <= self.hand_money:
             self.bet=1
             self.hand_money-=1
             return True
          return False

      def hit(self):
          self.add_card(self.shoe.draw_card())
          if self.reveal()>21:
             self.win= False
             return False
          return True

      def stand(self):
          pass

      def resolve_bet(self,dealer):
          dealer_value=dealer.reveal()
          player_value=self.reveal()

          if player_value>21:
             self.win= False
          elif dealer_value>21:
              self.win=True
          elif player_value==dealer_value:
               self.win= None
          elif player_value>dealer_value:
               self.win=True
          else:
              self.win=False

          money_change=0
          if self.win is True:
             money_change=self.bet*2
             self.hand_money+=money_change
          elif self.win is None:
              money_change=self.bet
              self.hand_money+=money_change
          self.bet=0
          return self.win,money_change

      def reset(self):
          self.win=None
          self.bet=0
          self.cards_in_hand=[]
          self.hand_value=0
          self.ace_count=0
          if self.hand_money<1:
             self.hand_money=1

class Dealer(Hand):

      def __init__(self,shoe):
          super().__init__(shoe)

      def reveal_one_card(self):
          if self.cards_in_hand:
              return self.cards_in_hand[0]
          return None

      def play_turn(self):
          while self.reveal()<17:
                self.add_card(self.shoe.draw_card())
          return self.reveal()

def simulate_hands(num_hands=100000):
    shoe=Shoe()
    player=Player(shoe)
    dealer=Dealer(shoe)

    results={}
    k=0
    while k < num_hands:
        player.reset()
        dealer.cards_in_hand=[]
        dealer.hand_value=0
        dealer.ace_count=0

        if not player.place_bet():
           break

        player.deal_initial_cards()
        dealer.deal_initial_cards()

        player_value=player.reveal()
        dealer_upcard=dealer.reveal_one_card()

        if dealer_upcard is None:
            k+=1
            continue

        dealer_upcard_value=Card.get_value_of_card(dealer_upcard)

        action=random.choice(['hit','stand'])

        key=(player_value,dealer_upcard_value)
        if key not in results:
            results[key]={
                'hit':{'money':[],'count':0},
                'stand':{'money': [], 'count':0}
            }

        if action =='hit':
            player.hit()
        else:
             player.stand()

        if player.reveal()<=21:
            dealer.play_turn()

        _,money_change=player.resolve_bet(dealer)

        results[key][action]['money'].append(money_change-1)
        results[key][action]['count']+=1
        k+=1

    print("\nResults Table: Average Money Change ($1 bet)")
    print("Player Value| Dealer Upcard| Hit Avg| Stand Avg| Best strat")
    print("-"*60)

    hit_avg=0
    stand_avg=0
    best_strat=''
    for (player_val,dealer_val), actions in sorted(results.items()):
        if actions['hit']['count']>0:
           hit_avg=sum(actions['hit']['money'])/actions['hit']['count']
        else:
            hit_avg=0

        if actions['stand']['count']>0:
            stand_avg=sum(actions['stand']['money'])/actions['stand']['count']
        else:
            stand_avg=0

        if hit_avg>stand_avg:
            best_strat='Hit'
        elif hit_avg<stand_avg:
             best_strat='stand'
        else:
             best_strat='Tie'

        print(f"{player_val:11} | {dealer_val:12} | {hit_avg:7.2f} | {stand_avg:8.2f} | {best_strat}")
if __name__=="__main__":
   print('Welcome to BlackJack!')
   print("1 for an interactive game")
   print("2 for a simulation")
   choice=input('1 or 2?')

   if choice=='2':
      simulate_hands(100000)
   else:
        shoe=Shoe()
        player=Player(shoe)
        dealer=Dealer(shoe)

        while True:
              print(f'\nYour Money: ${player.hand_money}')
              play=input("Enter to bet $1 or q to quit:")
              if play.lower()=="q":
                 print("bye")
                 break
              if not player.place_bet():
                 print("Insufficient funds! resetting to $1.")
                 player.hand_money=1
                 player.place_bet()

              player.reset()
              dealer.cards_in_hand=[]
              dealer.hand_value=0
              dealer.ace_count=0
              player.deal_initial_cards()
              dealer.deal_initial_cards()

              















        




