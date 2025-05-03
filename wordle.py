import random 
from rich import print



words = (
    'awake', 'blush', 'candy', 'dance', 'eager', 'flame', 'grape', 'haste', 'irate', 'jolly',
    'knack', 'latch', 'mango', 'noble', 'ocean', 'plume', 'quilt', 'racer', 'sable', 'tiger',
    'focal', 'evade', 'serve', 'karma', 'taiba', 'honey', 'timer'
)

class Wordle: # to make interface easier to use, we will create a class for the game
    def __init__(self):
        self.word= random.choice(words)
        self.num_guesses = 0
        self.guess_dict = {
            0: [" "]*5, # list with 5 elements
            1: [" "]*5,
            2: [" "]*5,
            3: [" "]*5,
            4: [" "]*5,
            5: [" "]*5,
        }

    def draw_board(self): # draw the board for the game
        for guess in self.guess_dict.values(): # in dicrtionary, values are the guesses, so we can iterate through them
            print(" | ".join(guess)) # join the guesses with a pipe character to make it look like a board
            print("============================") # print a line to separate the guesses


    def get_user_input(self): # get user input and check if it is valid
        user_guess = input (f"enter a 5 letter word:")
        while len(user_guess) != 5: # check if the input is valid
            user_guess = input (f"not valid, enter a 5 letter word:")

        user_guess = user_guess.lower() # convert the input to lowercase
        for idex , char in enumerate(user_guess): # iterate through the input and check if it is valid
            if char in self.word:
                if char == self.word[idex]:
                    char = f"[green]{char}[/]" #green: correct letter in correct position

            else:
                char = f"[yellow]{char}[/]" #yellow : correct letter in wrong position

            self.guess_dict[self.num_guesses][idex] = char
        
        self.num_guesses += 1 # increment the number of guesses
        return user_guess

    def play(self): # play the game 
        while True :
            self.draw_board()
            user_guess = self.get_user_input()

            if user_guess == self.word :
                self.draw_board()
                print(f"You win! the word was {self.word}")
                break 
                 
            if self.num_guesses > 5 :
                self.draw_board()
                print(f"You lose! the word was {self.word}")
                break
        
        