import random
import json
import time

class SlotMachine:
    def __init__(self, balance):
        self.balance = balance

    def play(self):
        while True:
            bet = float(input(f"Enter your bet amount (Available balance: {self.balance}): "))
            if bet > self.balance:
                print("Insufficient balance. Try again.")
                return

            self.balance -= bet
            symbols = ['🍒', '🍋', '🍊', '🔔', '⭐', '💎', '🍇','🍓']
            result = []

            
            print("Spinning...")
            for i in range(4):  # Roll one column at a time
                column_result = ''
                for step in range(30):  # Simulate rolling effect
                    column_result = random.choice(symbols)
                    print(" ".join(result + [column_result] + ['-'] * (3 - len(result))), end='\r', flush=True)
                    
                    # Gradually slow down the rolling speed
                    if step < 10:
                        time.sleep(0.05)  # Fast initial spin
                    elif step < 20:
                        time.sleep(0.1)  # Slightly slower
                    elif step < 25:
                        time.sleep(0.2)  # Noticeably slower
                    else:
                        time.sleep(0.3)  # Final slow roll
                        
                # Add the final symbol to the result
                result.append(column_result)
                time.sleep(0.3)  # Pause slightly before the next column starts

            print(" ".join(result))  # Final result display


            if len(set(result)) == 1:
                print("Jackpot! You win!")
                self.balance += bet * 10
            elif len(set(result)) == 2:  # Either "two pairs" or "two of a kind"
                counts = {symbol: result.count(symbol) for symbol in result}
                if 2 in counts.values() and list(counts.values()).count(2) == 2:
                    print("Two pairs! You win five times your bet back!")
                    self.balance += bet * 5
                else:
                    print("Nice! You win three times your bet back.")
                    self.balance += bet * 3
            elif len(set(result)) == 3:
                print("Superb! you get half your bet back.")
                self.balance += bet * 1.5
            else:
                print("Better luck next time!")

            print(f"New balance: {self.balance}")
            play_again = input("Do you want to play another round? (y/n): ").lower()
            if play_again != 'y':
                break