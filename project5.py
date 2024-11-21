# #Hangman game by joshieEE

# #create a module of random
# import random
# # create a random word choices

# word_list = ["storm","void","ember","earth"]
# words = random.choice(word_list)

# guessed_letters = []
# attempt = 6
# hidden_word = "_" * len(words)
# print("WElCOME TO HANGMAN GAME!!!")
# print("Try to guess a word,one letter at time")
# print(f"THe Word is {len(words)} letters")
# print(hidden_word)

# while attempt > 0 and "_" in hidden_word:
#     guess = input("\nGuess a letter!: ").lower()
    
#     if guess in guessed_letters:
#         print("You've already guess that letter Please Try AGain!")
#         continue

#     guessed_letters.append(guess)

#     if guess in words:
#         print(f"Good JOB! '{words}'is in the word ")
    
#     else:
#         attempt -= 1
#         print(f"Sorry, '{guess}' is not in the word. attempt left: {attempt}")
    
#     print(hidden_word)

# if "_" not in hidden_word:
#     print("\n Congratulation! You've guessed the word", words)
# else:
#     print("\n Out of attempt ", words)
        

import random

word_list = ["josh","ember","stormspirit"]
word = random.choice(word_list)

guess_letter = []
attempt = 6
hidden_letter = "_" * len(word)
print("WELCOME TO HANGMAN GAME!!")
print("Try to guess a hidden word")
print(f"The word is {len(word)} letter")
print(hidden_letter)

while attempt > 0 and "_" in hidden_letter:
    guess = input("\n Guess a Letter!: ").lower()

    if guess in guess_letter:
        print("YOu already guess the word Please Try again")
        continue

    guess_letter.append(guess)

    if guess in word:
        print(f"GOOD JOB BROTHER YOu guess '{word}' the word")
        if "ember" in word:
            print("YOwaimo Ember!")
        elif "stormspirit" is word:
            print("Yowaimo STORM")
        else:
            print("Yowaimo JOSh")

    else:
        attempt -= 1
        print(f"Srry, {guess} is not in the word, attempt left: {attempt} ")
    
    print(hidden_letter)

if "_" not in hidden_letter:
    print("\n Ongrats YOu've guess the word", word)
else:
    print("\nOut of attempt", word)

    







