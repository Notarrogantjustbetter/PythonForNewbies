# Small example of OOP in Python, if/else statements, random module and "f" string formatting.


import random


class Game:
    def __init__(self):
        pass

    def __str__(self):
        return "Lets play a game.Your answered number should be equal to mine, otherwise you will loose."

    @staticmethod
    def choose_wisely():
        number = random.randint(0, 10)
        my_guess = int(input("Choose a number from 0 to 10: "))
        print(f"My number is {number}, your guess is {my_guess}")
        if number == my_guess:
            return "Congrats, you win!"
        elif number != my_guess:
            try_again = input("Your answer is wrong, do you want to play again? Write yes or no : ")
            if try_again == "yes":
                return Game.choose_wisely()
            if try_again == "no":
                return "Okay, bye!"


random_number_game = Game()
print(random_number_game)
print(random_number_game.choose_wisely())


