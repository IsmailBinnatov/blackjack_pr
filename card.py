class Card:
    
    def __init__(self) -> None:
        suits = ['♠', '♥', '♦', '♣']
        values = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
        self.deck = [(f'{suit}.{value}')
                     for suit in suits for value in values]