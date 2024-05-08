from helpers import calculate_points


class Dealer:

    def __init__(self) -> None:
        self.hand = []

    def __str__(self) -> str:
        return f'Dealer\'s hand: {self.hand}. \nPoints: {calculate_points(self.hand)}'
