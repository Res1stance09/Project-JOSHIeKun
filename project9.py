import random

class Quotes_gene:
    def __init__(self):
        self.quotes = [
            {
                "text": "Be the change you wish to see in the world.",
                "author": "Mahatma Gandhi"
            },
            {
                "text": "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
                "author": "Albert Einstein"
            },
            {
                "text": "The only way to do great work is to love what you do.",
                "author": "Steve Jobs"
            },
            {
                "text": "In three words I can sum up everything I've learned about life: it goes on.",
                "author": "Robert Frost"
            },
            {
                "text": "The future belongs to those who believe in the beauty of their dreams.",
                "author": "Eleanor Roosevelt"
            }
        ]
        
        #add quotess
    def add_qoutes(self,text,author):
        self.quotes.append({"text": text, "author": author})
        #random choice
    def get_random_quotes(self):
        return random.choice(self.quotes)
        """get the quote above or iterate the self.quotes"""
    def get_quote_by_author(self,author):
        return [quote for quote in self.quotes if quote["author"].lower() == author.lower()]
            #display the quotes
    def display_quote(self,quote):
        return f'"{quote["text"]}" - {quote["author"]}'

if __name__ == "__main__":

    generator = Quotes_gene()
    
    quote = generator.get_random_quotes()
    print("\n RANDOM QUOTE:")
    print(generator.display_quote(quote))
    
    generator.add_qoutes("Stay hungry, stay foolish.", "Steve Jobs")
    
    steve_job_quotes = generator.get_quote_by_author("Steve Jobs")
    print("\nAll Steve Job quotes:") 
    
    for quote in steve_job_quotes:
        print(generator.display_quote(quote))
    
    
    
    generator.add_qoutes("Weakness of attitude becomes weakness of character.","Albert Eistein")
    albert_einstein_quote = generator.get_quote_by_author("Albert Einstein")
    print("\nAll Albert Eistein quotes:")
    
    for quote in albert_einstein_quote:
        print(generator.display_quote(quote))