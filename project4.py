# 
# 
#Import the random module
import random
# Create a function


def winner(player,computer):
    if player == computer:
        return "Its a Tie"
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
            (player == "scissor" and computer == "paper"):
        return "You Win!"
    else:
        return "Computer Win!"
    
#create choices
choices = ["rock", "paper","scissor"]

# create a loop in game

while True:
    player_input = input("Input a rock, paper, scissor (or type 'quit' to stop playing the game!) ").lower()
    
    if player_input == "quit":
        print("THank you for playing the game!")
        break

    if player_input not in choices:
        print("Invalid choices Please Try Again!  ")
        continue

    computer_choices = random.choice(choices)
    
    result = winner(player_input,computer_choices)
    print(f"\n Player choice You : {player_input} ")
    print(f"Computer Choice : {computer_choices}")
    print(result, "\n")     