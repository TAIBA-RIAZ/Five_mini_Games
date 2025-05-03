
# This is a simple Rock, Paper, Scissors game.
import random


def rock_paper_scissor():
    print("Welcome to Rock, Paper, Scissor!")

    r = 'rock'
    p = 'paper'
    s = 'scissor'
    all_choices = [r, p, s]

    user = input(f"enter your choice({r}, {p}, {s}): ")

    if user not in all_choices :
        print("Invalid choice!")
        return
    
    computer = random.choice(all_choices)
    print(f"User Chose : {user}, Computer chose: {computer}")

    # r>s, p>r, s>p
    if user == computer :
        print("It's a tie!")
    elif (user == r and computer == s) or (user == p and computer == r) or (user == s and computer == p):
        print("Hurrah! You won.")
    else:
        print("Oops! You lost.")

    