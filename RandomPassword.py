# Creating a strong password and remembering it is a tedious task.
# You can build a program that intakes some words from the user and then generates a random password using those words.
# The user can remember the password with the help of the words he gave as an input.

# The script idea is from internet, it's not mine.However, i decided to build the script, because it's somehow helpful
# for newbies.

import random


class Password:
    def __init__(self):
        pass

    def __str__(self):
        return "Lets create your password."

    @staticmethod
    def generator():
        print("Give me some words you will remember easily, 5 at least.")
        keywords = input("Write your keywords here: ")     # <-- Here you give some words which you can easily remember.

        first_collector = []
        first_collector.append(keywords.split(" "))

        second_collector = []                 # <-- The code from line 23 to 29 is my way of collecting the words.
        for elements in first_collector:      # <-- If you want you can search for better way to do it.
            for words in elements:
                second_collector.append(words)

        random_words = []
        counter = 0

        while True:                            # <-- Here we are in while loop until we have 3 from your keywords.
            if counter < 3:
                random_words.append(random.choice(second_collector))
                counter += 1
                continue
            break

        your_password = "".join(random_words)                           # <-- It is good to create a txt file where
        password_container = open("D:\\Programming\\Passwords.txt", "a")  # your password is saved immediately.
        password_container.write(your_password)
        password_container.close()
        print(f"Ready.This is your password {your_password}")
        print("The password is saved in the password container.")
        return "Bye."


p = Password()
print(p.generator())














