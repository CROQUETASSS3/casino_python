import random
class Craps:
    def __init__(self, balance):
        self.balance = balance

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

    def pass_line_bet(self, bet_amount):
        print("Roll the dice to establish a point!")
        input("Press Enter to roll the dice...")

        point = None
        while True:
            dice1, dice2 = self.roll_dice()
            roll_sum = dice1 + dice2
            print(f"You rolled: {dice1} + {dice2} = {roll_sum}")

            if point is None:
                if roll_sum in [7, 11]:
                    print("Congratulations! You win with a natural!")
                    return bet_amount * 2
                elif roll_sum in [2, 3, 12]:
                    print("Craps! You lose with a crap out!")
                    return 0
                else:
                    point = roll_sum
                    print(f"Point established: {point}")
            else:
                if roll_sum == point:
                    print("Congratulations! You win by hitting the point!")
                    return bet_amount * 2
                elif roll_sum == 7:
                    print("Seven out! You lose by hitting a seven!")
                    return 0

            input("Press Enter to roll again...")

    def play(self):
        print("\nWelcome to Craps!")
        while self.balance > 0:
            print(f"\nCurrent balance: {self.balance}")
            bet_amount = float(input("Enter your bet amount: "))
            if bet_amount > self.balance:
                print("Insufficient balance. Please enter a smaller amount.")
                continue

            result = self.pass_line_bet(bet_amount)
            self.balance += result - bet_amount
            print(f"New balance: {self.balance}")

            if self.balance <= 0:
                print("You're out of money! Game over.")
                break

            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                print(f"Thanks for playing! Your final balance is {self.balance}.")
                break
