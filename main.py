from gtn import guess_the_number
from rps import rock_paper_scissor
from wordle import Wordle
from connect_four import ConnectFour
from tictactoe import TicTacToe

while True:
    txt = """ Mini Games!!!
    - Guess the Number (1)
    - Rock, Paper, Scissor (2)
    - Wordle (3)
    - ConnectFour (4)
    - Tic Tac Toe (5)
Select a game (press a number or 'q' to quit): """
    
    value = input(txt)
    
    if value == "1":
        guess_the_number(10)
    elif value == "2":
        rock_paper_scissor()
    elif value == "3":
        game = Wordle()
        game.play()
    elif value == "4":
        game = ConnectFour()
        game.play()
    elif value == "5":
        game = TicTacToe()
        game.play()
    elif value == "q":
        break
# ask user for second input for upper limit
    # x = int(input("Enter the upper limit: "))
    # guess_the_number(x)
    # if value == "2":
    #     pass
    # elif value == "3":
    #     pass
    # elif value == "4":
    #     pass
    # elif value == "5":
    #     pass
    # elif value == "q":
    #     break
    # else:
    #     print("Invalid input. Please try again.")
    