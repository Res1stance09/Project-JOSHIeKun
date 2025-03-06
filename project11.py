class Money:
    def objects(self):
        self.principle = 0
        self.time = 0
        self.rate = 0
    
    def principles(self):
        while True:
            try:
                self.principle = int(input("Enter the principle amount: "))
                if self.principle > 0:
                    break
                else:
                    print("Principle must be greater than 0.")
            except ValueError:
                print("Please enter a Valid number and must be greater than 0")
    def times(self):
        while True:
            try:
                self.time = int(input("Enter the number of years: "))
                if self.time > 0:
                    break
                else:
                    print("Year is must be greater than 0")
            except ValueError:
                print("Please Enter a Valid number and must be greater than 0 ")
    
    def interest_rate(self):
        while True:
            try:
                self.rate = int(input("Enter the number of Interest rate '(%)' : "))
                if self.rate > 0:
                    break
                else:
                    print("Interest rate is must be greater than 0")
            except ValueError:
                print("Please Enter a Valid number and must be greater than 0")

    def calculate_interest(self):
        interest = self.principle * pow((1 + self.rate / 100),self.time)
        print(f"The Sample Interest in {self.time} year: ${interest:.2f}")
        return interest
        

def Main():
    josh = Money()
    josh.principles()
    josh.times()
    josh.interest_rate()
    josh.calculate_interest()

Main()
    