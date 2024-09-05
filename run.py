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


def print_board(board):
    """
    Print a grid to play noughts and crosses on. 9 blocks vertical split by dashes and horizontal split by pipe.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    """
    Check winning status on the printed board wether it is player i or j, checks both the rows of the board and the columns.
    """
    for i in range(3):
        if all([spott == player for spot in board[i]]) or \
            all(board[j][i] == player for j in range(3)):
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def check_draw(board):
    """
    Define the draw condition checking all spots are filled but the winning condition isn't met
    """
    return all([spot in ["X", "0"] for row in board for spot in row])