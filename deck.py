from player import Player
from dealer import Dealer
from random import shuffle, choice


class Deck:

    def __init__(self) -> None:
        suits = ['♠', '♥', '♦', '♣']
        values = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
        self.deck = [(f'{suit}.{value}')
                     for suit in suits for value in values]
        shuffle(self.deck)

        # Members object
        self.player = Player('noname')
        self.dealer = Dealer()

        # Issuing cards to the player and dealer
        self.dealer.hand.extend(choice(self.deck) for _ in range(2))
        self.deleted = self.dealer.hand.pop()
        self.player.hand.extend(choice(self.deck) for _ in range(2))
