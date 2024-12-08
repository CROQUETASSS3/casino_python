import random

class Blackjack:
    def __init__(self, balance):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.balance = balance

    def create_deck(self):
        return [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

    def deal_card(self, hand):
        if len(self.deck) == 0:
            self.deck = self.create_deck()
            random.shuffle(self.deck)
        hand.append(self.deck.pop())

    def calculate_hand(self, hand):
        value = sum(hand)
        ace_count = hand.count(11)
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        return value

    def show_hands(self, reveal_dealer=False):
        print(f"Player's hand: {self.player_hand} (Value: {self.calculate_hand(self.player_hand)})")
        if reveal_dealer:
            print(f"Dealer's hand: {self.dealer_hand} (Value: {self.calculate_hand(self.dealer_hand)})")
        else:
            print(f"Dealer's hand: [{self.dealer_hand[0]}, '?']")

    def play_round(self):
        bet = float(input(f"Enter your bet amount (Available balance: {self.balance}): "))
        while bet > self.balance:
            print("Insufficient balance. Try again.")
            bet = float(input(f"Enter your bet amount (Available balance: {self.balance}): "))

        self.player_hand = []
        self.dealer_hand = []
        for _ in range(2):
            self.deal_card(self.player_hand)
            self.deal_card(self.dealer_hand)

        self.show_hands()

        while True:
            move = input("Do you want to hit, stand, double down, split, or surrender? (h/s/d/p/r): ").lower()
            if move == 'h':
                self.deal_card(self.player_hand)
                self.show_hands()
                if self.calculate_hand(self.player_hand) > 21:
                    print("Player busts! Dealer wins.")
                    self.balance -= bet
                    return
            elif move == 's':
                break
            elif move == 'd':
                bet *= 2
                self.deal_card(self.player_hand)
                self.show_hands()
                break
            elif move == 'p':
                self.split()
                break
            elif move == 'r':
                print("Player surrenders. Dealer wins.")
                self.balance -= 0.5 * bet
                return
            else:
                print("Invalid move. Try again.")

        while self.calculate_hand(self.dealer_hand) < 17:
            self.deal_card(self.dealer_hand)

        self.show_hands(reveal_dealer=True)

        player_value = self.calculate_hand(self.player_hand)
        dealer_value = self.calculate_hand(self.dealer_hand)

        if player_value > 21:
            print("Player busts! Dealer wins.")
            self.balance -= bet
        elif dealer_value > 21 or player_value > dealer_value:
            print("Player wins!")
            self.balance += bet
        elif player_value < dealer_value:
            print("Dealer wins.")
            self.balance -= bet
        else:
            print("It's a tie!")

        print(f"New balance: {self.balance}")

    def split(self):
        if len(self.player_hand) != 2 or self.player_hand[0] != self.player_hand[1]:
            print("Splitting is only allowed with a pair of cards with the same value.")
            return

        self.player_hand = [self.player_hand[0], self.deck.pop()]
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)

        print("First hand after split:")
        self.show_hands()

        print("Second hand after split:")
        self.show_hands()

    def play(self):
        print("\nWelcome to Blackjack!")
        while self.balance > 0:
            self.play_round()
            play_again = input("Do you want to play another round? (y/n): ").lower()
            if play_again != 'y':
                print(f"Thanks for playing! Your final balance is {self.balance}.")
                break

    def dealer_play(self):
        while self.calculate_hand(self.dealer_hand) < 17:
            self.deal_card(self.dealer_hand)

        self.show_hands(reveal_dealer=True)
