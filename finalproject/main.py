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

