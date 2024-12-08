import random
class Poker:
    def __init__(self, balance):
        self.balance = balance

    def deal_hand(self):
        deck = [(self.card_name(rank), suit) for rank in range(2, 15) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']]
        random.shuffle(deck)
        return deck[:5]

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

    def evaluate_hand(self, hand):
        ranks = sorted([self.card_rank(card[0]) for card in hand])
        suits = [card[1] for card in hand]

        # Check for flush
        if len(set(suits)) == 1:
            flush = True
        else:
            flush = False

        # Check for straight
        if len(set(ranks)) == 5 and (max(ranks) - min(ranks) == 4):
            straight = True
        else:
            straight = False

        # Check for straight flush or royal flush
        if straight and flush:
            if min(ranks) == 10:
                return "Royal Flush", 250
            else:
                return "Straight Flush", 50

        # Check for four of a kind
        for rank in ranks:
            if ranks.count(rank) == 4:
                return "Four of a Kind", 25

        # Check for full house
        if len(set(ranks)) == 2:
            if ranks.count(ranks[0]) in [2, 3]:
                return "Full House", 9

        # Check for flush
        if flush:
            return "Flush", 6

        # Check for straight
        if straight:
            return "Straight", 4

        # Check for three of a kind
        for rank in ranks:
            if ranks.count(rank) == 3:
                return "Three of a Kind", 3

        # Check for two pair
        if len(set(ranks)) == 3:
            return "Two Pair", 2

        # Check for one pair
        if len(set(ranks)) == 4:
            return "One Pair", 1

        # Otherwise, return high card
        return "High Card", 0

    def card_rank(self, card):
        if card == 'Jack':
            return 11
        elif card == 'Queen':
            return 12
        elif card == 'King':
            return 13
        elif card == 'Ace':
            return 14
        else:
            return int(card)

    def play_round(self):
        print("\nDealing cards...")
        player_hand = self.deal_hand()
        dealer_hand = self.deal_hand()

        print(f"Dealer's hand: [Hidden Card, {dealer_hand[1]}, Hidden Card, Hidden Card, {dealer_hand[4]}]")
        print(f"Your hand: {player_hand}")

        # Betting phase
        bet_amount = float(input("Enter the amount you want to bet: "))
        while bet_amount > self.balance:
            print("Insufficient balance. Please enter a lower amount.")
            bet_amount = float(input("Enter the amount you want to bet: "))

        self.balance -= bet_amount
        print(f"Your bet: {bet_amount}")
        print(f"Your new balance: {self.balance}")

        # Allow the player to change some cards once
        change_cards = input("Do you want to change any cards? (y/n): ").lower()
        if change_cards == 'y':
            change_indices = input("Enter the indices of cards to change (e.g., '1 3 4'): ").split()
            change_indices = [int(index) - 1 for index in change_indices]

            for index in change_indices:
                player_hand[index] = self.deal_hand()[0]

            print(f"Your new hand: {player_hand}")

        player_strength, player_payout = self.evaluate_hand(player_hand)
        dealer_strength, dealer_payout = self.evaluate_hand(dealer_hand)

        print(f"Dealer's hand strength: {dealer_strength}")
        print(f"Your hand strength: {player_strength}")

        if player_strength > dealer_strength:
            print("Congratulations! You win!")
            self.balance += bet_amount * 2
        elif player_strength < dealer_strength:
            print("Sorry, you lose.")
        else:
            print("It's a tie! Bet amount returned.")

        print(f"Your new balance: {self.balance}")

    def play(self):
        print("\nWelcome to Five Card Draw Poker!")
        while self.balance > 0:
            print(f"\nCurrent balance: {self.balance}")
            play_round = input("Do you want to play a round? (y/n): ").lower()
            if play_round != 'y':
                print(f"Thanks for playing! Your final balance is {self.balance}.")
                break

            self.play_round()