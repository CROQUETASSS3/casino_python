import random

class Baccarat:
    
    def __init__(self, balance):
        self.balance = balance

    def create_deck(self):
        suits = '♠️ ♥️ ♦️ ♣️'.split()
        ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
        deck = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def deal_card(self, deck):
        return deck.pop()

    def calculate_hand_value(self, hand):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 1}
        return sum(values[card[0]] for card in hand) % 10

    def play_round(self):
        bet = float(input(f"Enter your bet amount (Available balance: {self.balance}): "))
        if bet > self.balance:
                print("Insufficient balance. Try again.")
                return
        self.balance -= bet
        print(f"\nStarting new round. Your balance: {self.balance}")

        deck = self.create_deck()
        player_hand = [self.deal_card(deck), self.deal_card(deck)]
        banker_hand = [self.deal_card(deck), self.deal_card(deck)]

        player_value = self.calculate_hand_value(player_hand)
        banker_value = self.calculate_hand_value(banker_hand)
        print(f"Player's hand: {player_hand}, value: {player_value}")
        print(f"Banker's hand: {banker_hand}, value: {banker_value}")

        if player_value in [8, 9] or banker_value in [8, 9]:
            # Natural win
            pass
        else:
            player_action = input("Do you want to hit or stand? (h/s): ").lower()
            if player_action == 'h':
                player_hand.append(self.deal_card(deck))
                player_value = self.calculate_hand_value(player_hand)
                print(f"Player draws a card: {player_hand}, value: {player_value}")

            banker_action = 'h' if banker_value < 6 else 's'
            if banker_action == 'h':
                banker_hand.append(self.deal_card(deck))
                banker_value = self.calculate_hand_value(banker_hand)
                print(f"Banker draws a card: {banker_hand}, value: {banker_value}")

        if player_value > banker_value:
            print("Player wins!")
            self.balance += bet*2
        elif player_value < banker_value:
            print("Banker wins.")
            
        else:
            print("Tie. No one wins.")
            self.balance+=bet

    def play(self):
        while self.balance > 0:
            bet = float(input(f"Enter your bet amount (Available balance: {self.balance}): "))
            if bet > self.balance:
                print("Insufficient balance. Try again.")
                continue
            self.play_round()
            play_again = input("Do you want to play another round? (y/n): ").lower()
            if play_again != 'y':
                break
        print(f"Game over. Your final balance: {self.balance}")