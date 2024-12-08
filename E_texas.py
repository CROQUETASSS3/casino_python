import random            
class TexasHoldem:
    def __init__(self, balance):
        self.balance = balance
        self.pot = 0
        self.community_cards = []

    def deal_hand(self):
        deck = [(self.card_name(rank), suit) for rank in range(2, 15) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']]
        random.shuffle(deck)
        return deck[:2]

    def deal_community_cards(self, num_cards):
        deck = [(self.card_name(rank), suit) for rank in range(2, 15) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']]
        random.shuffle(deck)
        self.community_cards = deck[:num_cards]

    def card_name(self, rank):
        if rank == 11:
            return 'Jack'
        elif rank == 12:
            return 'Queen'
        elif rank == 13:
            return 'King'
        elif rank == 14:
            return 'Ace'
        else:
            return str(rank)

    def bet(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        self.balance -= amount
        self.pot += amount
        return True

    def raise_bet(self, amount):
        # Placeholder method for raising bet
        print("Placeholder method for raising bet")

    def call_bet(self):
        # Placeholder method for calling bet
        print("Placeholder method for calling bet")

    def fold(self):
        # Placeholder method for folding
        print("Placeholder method for folding")

    def play_round(self):
        print("\nDealing cards...")
        player_hand = self.deal_hand()
        print(f"Your hand: {player_hand}")

        # Betting phase
        bet_amount = float(input("Enter the amount you want to bet: "))
        while not self.bet(bet_amount):
            bet_amount = float(input("Enter the amount you want to bet: "))

        print(f"Your bet: {bet_amount}")
        print(f"Your new balance: {self.balance}")

        # Deal community cards
        self.deal_community_cards(3)
        print(f"Community cards: {self.community_cards}")

        # Placeholder for actions
        action = input("Enter your action (bet/raise/call/fold): ").lower()
        if action == 'bet':
            amount = float(input("Enter amount: "))
            self.bet(amount)
        elif action == 'raise':
            amount = float(input("Enter amount to raise: "))
            self.raise_bet(amount)
        elif action == 'call':
            self.call_bet()
        elif action == 'fold':
            self.fold()

        # Placeholder for determining winner
        winner = 'Player'  # Dummy winner

        # Placeholder for handling winner
        if winner == 'Player':
            print("Congratulations! You win!")
            self.balance += self.pot * 2
        else:
            print("Sorry, you lose.")

        print(f"Your new balance: {self.balance}")

    def play(self):
        print("\nWelcome to Texas Hold'em!")
        while self.balance > 0:
            print(f"\nCurrent balance: {self.balance}")
            play_round = input("Do you want to play a round? (y/n): ").lower()
            if play_round != 'y':
                print(f"Thanks for playing! Your final balance is {self.balance}.")
                break

            self.play_round()