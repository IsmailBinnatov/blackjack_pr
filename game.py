from deck import *
from constants import *
from time import sleep


class Game:

    def __init__(self) -> None:
        self.deck = Deck()
        self.player = self.deck.player
        self.dealer = self.deck.dealer

    def calculate_points(self, hand):
        total_points = 0

        for card in hand:
            value = card.split('.')[1]
            if value.isdigit():
                total_points += int(value)
            elif isinstance(value, str) and value != 'A':
                total_points += 10
            elif value == 'A':
                if total_points >= 11:
                    total_points += 1
                else:
                    total_points += 11

        return total_points

    def player_turn(self) -> None:
        while True:
            if self.calculate_points(self.player.hand) == 21:
                break
            sleep(0.8)
            action = input('Your turn: (h)it or (s)tand?: ').lower()

            if action == 'h':
                self.player.hand.append(choice(self.deck.deck))
                print()  # for empty line
                sleep(0.8)
                print(YELLOW + 'You drew a card...' + RESET)
                print()  # for empty line
                sleep(0.8)
                print(f'Your hand: {self.player.hand}. \nYour Points: {YELLOW}{
                      self.calculate_points(self.player.hand)}{RESET}')
                print()  # for empty line
                if self.calculate_points(self.player.hand) > 21:
                    sleep(0.8)
                    print(RED + 'Overreach!' + RESET)
                    print()  # for empty line
                    break
            elif action == 's':
                sleep(0.8)
                print(YELLOW + '\nYou stand.\n' + RESET)
                break
            else:
                sleep(0.8)
                print('Invalid input! Enter (h) for hit or (s) for stand.')

    def dealer_turn(self):
        self.dealer.hand.append(self.deck.deleted)
        sleep(0.8)
        print(YELLOW + 'Dealer shows the second card...' + RESET)
        print()  # for empty line
        sleep(0.8)
        print(f'Dealer\'s hand: {self.dealer.hand}. \nDealer Points: {YELLOW}{
            self.calculate_points(self.dealer.hand)}{RESET}')
        print()  # for empty line
        while self.calculate_points(self.dealer.hand) < 17:
            self.dealer.hand.append(choice(self.deck.deck))
            sleep(0.8)
            print(YELLOW + 'Dealer draws a card...' + RESET)
            print()  # for empty line
            sleep(0.8)
            print(f'Dealer\'s hand: {self.dealer.hand}. \nDealer Points: {YELLOW}{
                  self.calculate_points(self.dealer.hand)}{RESET}')
            print()  # for empty line
            if self.calculate_points(self.dealer.hand) > 21:
                sleep(0.8)
                print('Dealer overdraw!', GREEN + 'You win!' + RESET)
                print()  # for empty line
                break

    def game_loop(self):
        print()  # for empty line
        sleep(0.5)
        print(YELLOW + 'Game starts!' + RESET)
        print()  # for empty line
        sleep(0.8)
        print(f'Player\'s hand: {self.player.hand}\nPlayer Points: {YELLOW}{self.calculate_points(self.player.hand)}{RESET}')
        print()  # for empty line
        if self.calculate_points(self.player.hand) == 21:
            print(BLUE + '- Blackjack! -' + RESET)
        print()  # for empty line
        sleep(0.8)
        print(f'Dealer\'s hand: {self.dealer.hand + ['?']}\nDealer Points: {YELLOW}{
              self.calculate_points(self.dealer.hand)}{RESET}')
        print()  # for empty line
        if self.calculate_points(self.dealer.hand) == 21:
            print(YELLOW + '- Blackjack! -' + RESET)
        print()  # for empty line

        self.player_turn()
        if self.calculate_points(self.player.hand) <= 21:
            self.dealer_turn()

        player_points = self.calculate_points(self.player.hand)
        dealer_points = self.calculate_points(self.dealer.hand)
        if player_points <= 21 and player_points > dealer_points:
            sleep(0.8)
            print(GREEN + 'You win!' + RESET)
            print()  # for empty line
        elif dealer_points <= 21 and (player_points > 21 or dealer_points > player_points):
            sleep(0.8)
            print(RED + 'Dealer wins!' + RESET)
            print()  # for empty line
        elif player_points == dealer_points:
            sleep(0.8)
            print('Tie!')
            print()  # for empty line

        sleep(0.8)
        print(f'Final hands:\nPlayer hands: {
              self.player.hand}\nDealer hands: {self.dealer.hand}')
        print()  # for empty line


g = Game()
g.game_loop()
