import time
import os
import random

def spin_row():
    symbols = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎", "7️⃣"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("=============")
    print(" | ".join(row))
    print("=============")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_animation():
    frames = ["| ", "/ ", "— ", "\\ "]
    for _ in range(5):
        for frame in frames:
            print(f"\rSpinning {frame}", end="", flush=True)
            time.sleep(0.1)
    print("\r          ", end="", flush=True)

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        if row[0] == "🍋":
            return bet * 5
        if row[0] == "🍊":
            return bet * 8
        if row[0] == "🍇":
            return bet * 8
        if row[0] == "🔔":
            return bet * 10
        if row[0] == "💎":
            return bet * 15
        if row[0] == "7️⃣":
            return bet * 20
    return 0

def play_game():
    current_balance = 100

    print("********************")
    print("Welcome to Slot Machine Game!")
    print("|🍒|🍋|🍊|🍇|🔔|💎|7️⃣|")
    print("---------------------------")

    while current_balance > 0:
        print(f"Your current balance is ${current_balance}")

        bet = input("Enter your amount to bet: ")

        if not bet.isdigit():
            print("Bet must be a valid number!")
            continue

        bet = int(bet)

        if bet <= 0:
            print("Your bet must be greater than 0 to proceed.")
            continue

        if bet > current_balance:
            print("Insufficient balance.")
            continue
        
        display_animation()
        row = spin_row()
        print_row(row)

        current_balance -= bet

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
            current_balance += payout
        else:
            print("Sorry, you lost this round! 😊")

    print("You're out of money! Game over.")

def main():
    clear()
    
    attempt = 3
    code = "MyloveMau"
    code_used = False

    while attempt > 0:
        play_game()
        attempt -= 1

        if attempt == 0:
            if not code_used:
                voucher = input("You're out of attempts! Do you have a code for extra 3 attempts? (Yes/No): ").lower()
                if voucher in ("yes", "y"):
                    user_code = input("Enter your code: ")
                    if user_code.lower() == code.lower():
                        attempt += 3
                        code_used = True
                        print(f"Code is valid. You have {attempt} more attempts to continue.")
                    else:
                        print("Invalid code. Game Over.")
                        break
                else:
                    print("Game Over!")
                    break
            else:
                print("You've already used the code! Game Over!")
                break

        resume = input("Would you like to continue the game? (Yes/No): ").lower()
        if resume not in ("yes", "y"):
            print("Better luck next time!")
            break
        else:
            print(f"You have {attempt} attempt(s) left.\n")
            

if __name__ == "__main__":
    main()