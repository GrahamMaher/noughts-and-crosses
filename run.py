import random

def welcome_message(player_name):
    """
    Print players name into the welcome message as well as give a brief desciption on how to play.
    """
    print(f"Welcome to Noughts and Crosses, {player_name}.")
    print(f"You will be playing as Player X against the computer Player O.")
    print(f"How to play - To make your move, choose the position of where you want to place your X and then enter the row and column number. The numbers must be between 1 and 3 and seperated by a space.")
    print(f"The winner is the first to align three marks either horizontally in a row, vertically in a column, or diagonally.")
    print(f"Let the games begin, may the best person (or pc) win!")
