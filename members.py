# include Player and Dealer class

class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.hand = []

    def __str__(self) -> str:
        return f'{self.name}\'s hand: {self.hand}'


class Dealer:

    def __init__(self) -> None:
        self.hand = []

    def __str__(self) -> str:
        return f'Dealer\'s hand: {self.hand}'
