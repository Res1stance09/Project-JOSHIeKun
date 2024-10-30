# # def add(x,y):
# #     return x + y
# # def subtract(x,y):
# #     return x - y
# # def multiply(x,y):
# #     return x * y
# # def divide(x,y):
# #     if y == 0:
# #         return "Error!: Divide the 0 is undefined."
# #     return x / y

# # def calculator():
# #     print("Select the Operation Below")
# #     print("1. Add")
# #     print("2. Subtract")
# #     print("3. Multiply")
# #     print("4. Divide")

# #     choice = float("Enter Choice (1/2/3/4)")

# #     if choice not in [1,2,3,4]:
# #         print("Invalid Input")
# #         return

# #     try:
# #         num1 = float(input("Enter a first Number: "))
# #         num2 = float(input("Enter a second Number: "))
# #     except ValueError:
# #         print("Invalid input: Please Try Again!")
# #         return

# #     if choice == '1':
# #         print("Result is :", add(num1,num2))   

# reader = open('New folder/HTML/py/3.py')
# count = 0   
# for line in reader:
#     word = line.split()
#     count += (len(word))
# print(count)

# line = "city; then of the figure of a man walking swiftly; then of a child"
# # Divide the line into a list of words
# word_list = line.split()
# # Make an empty dictionary
# frequency_dict = {}
# for word in word_list:
#     # Add each word to the dictionary with a value of 1.
#     frequency_dict[word] = 1
    
# print(frequency_dict)


# Mad Libs game

# Define a function to play Mad Libs
def mad_libs():
    # Prompt the player for words
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adverb1 = input("Enter an adverb: ")
    place = input("Enter a place: ")
    noun2 = input("Enter another noun: ")
    adjective2 = input("Enter another adjective: ")

    # Mad Libs story template
    story = f"""
    Today's im mad because i was {adjective1} earlier. In {noun1} are so noice when im {verb1}
    they talk aloud about {adverb1} last thursday. In {place} City {noun2} the City of Mayor he announce
    the cancellation of classes in Calamba due to {adjective2} the Holliday of death krrr!!.
    """

    # Print the completed Mad Libs story
    print("\nHere's your story:")
    print(story)

# Run the Mad Libs game
mad_libs()
