

# this file is about to guess the next number in a sequence of numbers
import random


def guess_the_number(x):
    print("Let's play Guess the Number!")

    random_number = random.randint(0, x)
    num_guesses = 0
    while True:
        guess = int(input(f"Guess a number between 0 and {x} : ")) # make this str into int to avoid crash in code
        num_guesses = +1

        if guess == random_number:
            print(f"Congratulations! the number is {random_number}")
            break
        elif guess < random_number:
            print(f'Oops! Too Low')
        else :
            print(f"Too High!")


