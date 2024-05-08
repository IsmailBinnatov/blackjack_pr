from deck import *
from helpers import calculate_points
from time import sleep


class Game:

    def __init__(self) -> None:
        self.deck = Deck()
        self.player = self.deck.player
        self.dealer = self.deck.dealer

    def player_turn(self):
        while True:
            sleep(0.5)
            action = input('Your turn: (h)it or (s)tand?: ').lower()

            if action == 'h':
                self.player.hand.append(choice(self.deck.deck))
                print()  # for empty line
                sleep(0.5)
                print('You drew a card...')
                print()  # for empty line
                sleep(0.5)
                print(f'Your hand: {self.player.hand}. \nYour Points: {
                      calculate_points(self.player.hand)}')
                print()  # for empty line
                if calculate_points(self.player.hand) > 21:
                    sleep(0.5)
                    print('Overreach!')
                    print()  # for empty line
                    break
            elif action == 's':
                sleep(0.5)
                print('\nYou stand.\n')
                break
            else:
                sleep(0.5)
                print('Invalid input! Enter (h) for hit or (s) for stand.')

    def dealer_turn(self):
        while calculate_points(self.dealer.hand) < 17:
            self.dealer.hand.append(choice(self.deck.deck))
            sleep(0.5)
            print('Dealer draws a card...')
            print() # for empty line
            sleep(0.5)
            print(f'Dealer\'s hand: {self.dealer.hand}. \nDealer Points: {
                  calculate_points(self.dealer.hand)}')
            print()  # for empty line
            if calculate_points(self.dealer.hand) > 21:
                sleep(0.5)
                print('Dealer overdraw! You win!')
                print()  # for empty line
                break

    def game_loop(self):
        print()  # for empty line
        sleep(0.5)
        print('Game starts!')
        print()  # for empty line
        sleep(0.5)
        print(f'Player\'s hand: {self.player.hand}\nPlayer Points: {
              calculate_points(self.player.hand)}')
        print()  # for empty line
        sleep(0.5)
        print(f'Dealer\'s hand: {self.dealer.hand}\nDealer Points: {
              calculate_points(self.dealer.hand)}')
        print()  # for empty line

        self.player_turn()
        if calculate_points(self.player.hand) <= 21:
            self.dealer_turn()

        player_points = calculate_points(self.player.hand)
        dealer_points = calculate_points(self.dealer.hand)
        if player_points <= 21 and player_points > dealer_points:
            sleep(0.5)
            print('You win!')
        elif dealer_points <= 21 and (player_points > 21 or dealer_points > player_points):
            sleep(0.5)
            print('Dealer wins!')
            print()  # for empty line
        elif player_points == dealer_points:
            sleep(0.5)
            print('Tie!')
            print()  # for empty line

        sleep(0.5)
        print(f'Final hands:\nPlayer hands: {
              self.player.hand}\nDealer hands: {self.dealer.hand}')
        print()  # for empty line


g = Game()
g.game_loop()
