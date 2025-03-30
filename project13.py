import time

questions = ("What is the square root of 64?: ",
            "Which country is famous for inventing pizza?: ",
            "What is the longest river in the world?: ",
            "Who discovered gravity when an apple fell on his head?: ",
            "What gas do plants absorb from the atmosphere?: "
)

options = (
    ("A. 6 B. 7 C. 8 D. 9 "),
    ("A. Spain B. Italy C. France D. Greece "),
    ("A. Amazon River  B. Nile River  C. Yangzte River D. Mississippi River "),
    ("A. Albert Einstein B. Isaac Newton  C. Galileo Galilei D. Nikola Tesla "),
    ("A. Oxygen B. Carbon Dioxide C. Nitrogen  D. Hydrogen ")
    )

answers = ("C", "B", "A", "A", "B")
guesses = []
score = 0
question_num = 0

#start time
start_time = time.time()
print("Quiz started! Timer running...")


for question in questions:
    print("-----------------------------------")
    print(question)
    print(options[question_num])
    
    while True:
        guess = input("\nEnter You're answer: ").upper().strip()
        try:
            if guess.isdigit():
                raise ValueError("Invalid input. Please choose ' A. B. C. D. ' instead")
            break
        except ValueError as e:
            print(e)
        guesses.append(guess)
        
    if guess == answers[question_num]:
        score += 1
        print("You're Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    
    print()
    question_num += 1
    
#end time
end_time = time.time()
elapse_time = end_time - start_time

total = (score / len(answers)) * 100        
print(f"The total score you got {total}%")
print(f"The time you take the quizzes: {elapse_time:.2f} seconds")

if total >= 80 and elapse_time < 60:
    print("Great Job you finished it quickly!")
elif total >= 80:
    print("Great accuracy! but try to improve your speed")
elif elapse_time < 60:
    print("You're quick but try to improve your answers!")
else:
    print("Keep practicing!")