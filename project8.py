class Dino:
    def __init__(self, name):
        self.name = name
        self.jump = 0
        self.down = 0

    def info(self):
        return "Dino is a Reptile"

class User(Dino):
    def __init__(self, name):
        super().__init__(name)

    def start(self):
        print("Welcome to DINO Jump Down Game!")
        print(f"\nWelcome, {self.name}! Your adventure begins...\n")

        while True:
            print("\nChoose an action:")
            print("Input ('j') to jump or ('d') to move down. Input ('q') to quit.")
            user_input = input("You: ").lower()

            if user_input == 'j':
                self.jump += 1
                print(f"{self.name} jumped! Total jumps: {self.jump}")
            elif user_input == 'd':
                self.down += 1
                print(f"{self.name} moved down! Total downs: {self.down}")
            elif user_input == 'q':
                print("\nGame Over! Here are your stats:")
                print(f"Total Jumps: {self.jump}")
                print(f"Total Downs: {self.down}")
                break
            else:
                print("Invalid input. Please try again.")

# Run the game
if __name__ == "__main__":
    player_name = input("Enter your Dino's name: ")
    player = User(player_name)
    player.start()
