from helpers import calculate_points


class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.hand = []

    def __str__(self) -> str:
        return f'{self.name}\'s hand: {self.hand}. \nYour Points: {calculate_points(self.hand)}'
