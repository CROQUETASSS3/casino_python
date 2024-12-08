import random
import json
import time
from A_slots import SlotMachine
from B_roulette import Roulette
from C_craps import Craps
from D_poker import Poker
from E_texas import TexasHoldem
from F_blackjack import Blackjack
from G_baccarat import Baccarat

class Casino:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        try:
            with open("./users.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open("./users.json", "w") as file:
            json.dump(self.users, file)

    def login(self):
        username = input("Enter your username: ")
        if username in self.users:
            password = input("Enter your password: ")
            if self.users[username]["password"] == password:
                print(f"Welcome back, {username}!")
                return username
            else:
                print("Incorrect password. Try again.")
                return self.login()
        else:
            print("Username not found. Do you want to create a new account? (y/n)")
            if input().lower() == 'y':
                return self.create_account()
            else:
                return self.login()

    def create_account(self):
        username = input("Choose a username: ")
        if username in self.users:
            print("Username already exists. Try again.")
            return self.create_account()
        password = input("Choose a password: ")
        self.users[username] = {"password": password, "balance": 1000}
        self.save_users()
        print(f"Account created! Welcome, {username}!")
        return username

    def play_game(self):
        username = self.login()
        balance = self.users[username]["balance"]
        while True:
            print(f"\nWelcome to the Casino, {username}!")
            print("1. Play Slots")
            print("2. Play Roulette")
            print("3. Play Craps")
            print("4. Play Five-Card Draw Poker")
            print("5. Play Texas Hold'em")
            print("6. Play Blackjack")
            print("7. Play Baccarat")
            print("8. Save and Exit")

            choice = input("Choose a game to play (1-8): ")

            if choice == '1':
                game = SlotMachine(balance)
                game.play()
                balance = game.balance
            elif choice == '2':
                game = Roulette(balance)
                game.play()
                balance = game.balance
            elif choice == '3':
                game = Craps(balance)
                game.play()
                balance = game.balance
            elif choice == '4':
                game = Poker(balance)
                game.play()
                balance = game.balance
            elif choice == '5':
                game = TexasHoldem(balance)
                game.play()
                balance = game.balance
            elif choice == '6':
                game = Blackjack(balance)
                game.play()
                balance = game.balance
            elif choice == '7':
                game = Baccarat(balance)
                game.play()
                balance = game.balance
            elif choice == '8':
                self.users[username]["balance"] = balance
                self.save_users()
                print(f"Thanks for playing! Your final balance is {balance}.")
                break
            else:
                print("Invalid choice. Please choose again.")
        self.save_users()


# Start the casino
casino = Casino()
casino.play_game()
