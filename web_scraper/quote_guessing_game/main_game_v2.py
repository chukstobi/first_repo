from bs4 import BeautifulSoup
from csv import DictReader,DictWriter
import requests
import random

BASE_URL = "http://quotes.toscrape.com"

class QuoteGuessingGame:
    def read_quotes(self, filename):
        with open(filename, "r") as file:
            csv_reader = DictReader(file)
            return list(csv_reader)
    
    def player_detail(self):
        player_name = input("Please enter name ")
        player_score = 0
        
        player_file = open("player_details.csv",'a')
        player_file.write(f"{player_name},{player_score}")

    def main_game(self, quotes):
        filename = open("player_details.csv",'r')
        player_detail = []
        for file in filename:
            s = file.split(",")
            name = s[0]
            score = int(s[1])
            detail = [name,score]
            player_detail.append(detail)
            print(name,":",score)
        player_name = player_detail[0][0]
        player_score = int(player_detail[0][1])
        new_score = 0
        quote = random.choice(quotes)
        remaining_guesses = 4
        print(f"Here's a quote\n{quote['text']}")
        print(quote['author'])
        guess = ''

        if guess.lower() == quote["author"].lower() and remaining_guesses > 0:
            print("You win")
            new_score += 5
        elif guess.lower() != quote["author"].lower() and remaining_guesses > 0:
            guess = input(f"Who said this quote?\nGuesses remaining:{remaining_guesses}\n> ")
            remaining_guesses -= 1
            if remaining_guesses == 3:
                res = requests.get(f"{BASE_URL}{quote['bio-link']}")
                soup = BeautifulSoup(res.text, 'html.parser')
                birth_date = soup.find(class_='author-born-date').get_text()
                birth_place =soup.find(class_='author-born-location').get_text()
                print(f"Here's a hint: The author was born on {birth_date} {birth_place}")
            elif remaining_guesses == 2:
                print(f"Here's a hint: The author first name starts with {quote['author'][0]}")
            elif remaining_guesses == 1:
                last_initial = quote["author"].split(" ")[1][0]
                print(f"Here's a hint: The author last name starts with {last_initial}")
            else:
                print(f"You Loss.\nAnswer: {quote['author']}")
            
            if new_score > player_score:
                player_score = new_score
                player_file = open("player_details.csv",'w')
                player_file.write(f"{player_name},{player_score}")
            else:
                pass

    def begin(self):
        self.player_detail
        quotes = self.read_quotes("all_quotes.csv")
        self.main_game(quotes)

game = QuoteGuessingGame()
game.begin()

