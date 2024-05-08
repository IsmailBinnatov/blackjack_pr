from deck import *
from helpers import calculate_points


class Game:

    def __init__(self) -> None:
        self.deck = Deck()
        self.player = self.deck.player
        self.dealer = self.deck.dealer

    def player_turn(self):
        while True:
            action = input('Your turn: (h)it or (s)tand?: ').lower()
            if action == 'h':
                self.player.hand.append(choice(self.deck.deck))
                print('You drew a card!')
                print(f'Your hand: {self.player.hand}. \nYour Points: {
                      calculate_points(self.player.hand)}')
                if calculate_points(self.player.hand) > 21:
                    print('Overreach! Dealer wins!')
                    break
            elif action == 's':
                print('You stand.')
                break
            else:
                print('Invalid input! Enter (h) for hit or (s) for stand.')

    def dealer_turn(self):
        while calculate_points(self.dealer.hand) < 17:
            self.dealer.hand.append(choice(self.deck.deck))
            print('Dealer draws a card')
            print(f'Dealer\'s hand: {self.dealer.hand}. \nDealer Points: {
                  calculate_points(self.dealer.hand)}')
            if calculate_points(self.dealer.hand) > 21:
                print('Dealer overdraw! You win!')
                break
    
    def game_loop(self):
        pass



g = Game()
# g.player_turn()
# g.dealer_turn()
