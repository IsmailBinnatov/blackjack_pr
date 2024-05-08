from card import Card
from members import Player, Dealer
from random import shuffle, choice


class Deck:

    def __init__(self) -> None:
        self.deck = Card().deck
        shuffle(self.deck)
        self.player = Player('NoName')
        self.dealer = Dealer()

    # def __str__(self) -> str:     # for checikng deck
    #     return str(self.deck)

    def card_issue(self):

        for _ in range(2):
            self.player.hand.append(choice(self.deck))
            self.dealer.hand.append(choice(self.deck))


d = Deck()
d.card_issue()
print(d.player)
print(d.dealer)
# print(d.__str__())