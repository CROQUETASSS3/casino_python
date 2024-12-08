import random
class Roulette:
    def __init__(self, balance):
        self.wheel = list(range(37))  # 0-36
        self.colors = ['Green'] + ['Red', 'Black'] * 18
        self.balance = balance

    def spin_wheel(self):
        return random.choice(self.wheel)

    def place_bets(self):
        bets = []
        while True:
            print("\nBetting options:")
            print("1. Number (0-36)")
            print("2. Color (Red, Black, Green)")
            print("3. Odd or Even")
            print("4. High or Low (1-18, 19-36)")
            while True:
                try:
                    bet_type = int(input("Choose your bet type (1-4): "))
                    break
                except:
                    print('please choose a valid input between one and four!')
                    continue
            amount = float(input(f"Enter bet amount (Available balance: {self.balance}): "))
            if amount > self.balance:
                print("Insufficient balance. Try again.")
                continue

            if bet_type == 1:
                number = int(input("Pick a number (0-36): "))
                bets.append(('number', number, amount))
            elif bet_type == 2:
                color = input("Pick a color (Red, Black, Green): ").capitalize()
                bets.append(('color', color, amount))
            elif bet_type == 3:
                parity = input("Pick Odd or Even: ").capitalize()
                bets.append(('parity', parity, amount))
            elif bet_type == 4:
                range_bet = input("Pick High or Low: ").capitalize()
                bets.append(('range', range_bet, amount))
            else:
                print("Invalid bet type.")
                continue
            
            self.balance -= amount
            
            more_bets = input("Do you want to place another bet? (y/n): ").lower()
            if more_bets != 'y':
                break
        
        return bets

    def check_bets(self, bets, result, color_result):
        for bet in bets:
            bet_type, bet_value, amount = bet
            win = False
            if bet_type == 'number' and bet_value == result:
                win = True
                payout = amount * 35
            elif bet_type == 'color' and bet_value == color_result:
                win = True
                payout = amount * 2
            elif bet_type == 'parity' and ((bet_value == 'Odd' and result % 2 != 0) or (bet_value == 'Even' and result % 2 == 0)):
                if result != 0:  # 0 is neither odd nor even
                    win = True
                    payout = amount * 2
            elif bet_type == 'range' and ((bet_value == 'High' and 19 <= result <= 36) or (bet_value == 'Low' and 1 <= result <= 18)):
                win = True
                payout = amount * 2

            if win:
                print(f"You won {payout} on {bet_type} {bet_value}!")
                self.balance += payout
            else:
                print(f"You lost {amount} on {bet_type} {bet_value}.")

    def play_round(self):
        print(f"\nCurrent balance: {self.balance}")
        bets = self.place_bets()
        result = self.spin_wheel()
        color_result = self.colors[result]
        print(f"\nThe ball landed on {result} ({color_result}).\n")
        self.check_bets(bets, result, color_result)
        print(f"New balance: {self.balance}")

    def play(self):
        while self.balance > 0:
            self.play_round()
            if self.balance <= 0:
                print("You're out of money! Game over.")
                break

            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                print(f"Thanks for playing! Your final balance is {self.balance}.")
                break
