# include Player and Dealer class

def calculate_points(hand):
    total_points = 0

    for card in hand:
        value = card.split('.')[1]
        if value.isdigit():
            total_points += int(value)
        elif isinstance(value, str):
            total_points += 10
        elif value == 'A':
            total_points += 11

    return total_points


class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.hand = []

    def __str__(self) -> str:
        return f'{self.name}\'s hand: {self.hand}. \nPoints: {calculate_points(self.hand)}'


class Dealer:

    def __init__(self) -> None:
        self.hand = []

    def __str__(self) -> str:
        return f'Dealer\'s hand: {self.hand}. \nPoints: {calculate_points(self.hand)}'
