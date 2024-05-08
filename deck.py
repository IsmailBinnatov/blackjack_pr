from members import Player, Dealer
from random import shuffle, choice


class Deck:

    def __init__(self) -> None:
        suits = ['♠', '♥', '♦', '♣']
        values = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
        self.deck = [(f'{suit}.{value}')
                     for suit in suits for value in values]
        shuffle(self.deck)

        # Members object
        self.player = Player('NoName')
        self.dealer = Dealer()

    def card_issue(self):

        for _ in range(2):
            self.player.hand.append(choice(self.deck))
            self.dealer.hand.append(choice(self.deck))


d = Deck()
d.card_issue()
print(d.player)
print(d.dealer)
# print(d.__str__())
