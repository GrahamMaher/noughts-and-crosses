"""
Code to play noughts and crosses, made with python.
"""

import random


from colorama import init, Fore, Style


init(autoreset=True)


X_COLOUR = Fore.LIGHTCYAN_EX
O_COLOUR = Fore.LIGHTRED_EX


def welcome_message(player_name):
    """
    Print player's name in the welcome message.
    Give a brief description of how to play.
    """
    print(f"Welcome to Noughts and Crosses, {player_name}.")
    print("You will be playing as Player X against the computer Player O.")
    print(
        "How to play - To make your move, choose the position where you "
        "want to place your X and then enter the row and column number. "
        "The numbers must be between 1 and 3 and separated by a space."
    )
    print(
        "The winner is the first to align three marks either horizontally "
        "in a row, vertically in a column, or diagonally."
    )
    print("Let the games begin, may the best person (or PC) win!")


def print_board(board):
    """
    Print a grid to play noughts and crosses on.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    """
    Check winning status on the printed board whether it is player X or O.
    Checks both the rows of the board and the columns.
    """
    player_mark = (
        X_COLOUR + "X" + Style.RESET_ALL
        if player == "X"
        else O_COLOUR + "O" + Style.RESET_ALL
    )

    for i in range(3):
        if all([spot == player_mark for spot in board[i]]) or all(
            board[j][i] == player_mark for j in range(3)
        ):
            return True

    if (
        board[0][0] == board[1][1] == board[2][2] == player_mark
        or board[0][2] == board[1][1] == board[2][0] == player_mark
    ):
        return True

    return False


def check_draw(board):
    """
    Define the draw condition.
    Check if all spots are filled but the winning condition isn't met.
    """
    return all(
        [
            spot in [
                X_COLOUR + "X" + Style.RESET_ALL,
                O_COLOUR + "O" + Style.RESET_ALL,
            ]
            for row in board
            for spot in row
        ]
    )


def get_player_move(player_name):
    """
    Prompt user to input a move.
    Validate whether the input is valid, return it or print an error message.
    """
    while True:
        move = input(
            f"{player_name} (Player X), enter your move (row and column): "
        )
        try:
            row, col = map(int, move.split())
            if row in range(1, 4) and col in range(1, 4):
                return row - 1, col - 1
            else:
                print(
                    "Invalid input. Please select a number between 1 and 3 "
                    "for row and column values."
                )
        except ValueError:
            print("Invalid input. Enter 2 numbers separated by a space.")


def get_computer_move(board):
    """
    Generate a list of all available moves on the board.
    Randomly return a move for the opponent player.
    """
    available_moves = [
        (i, j) for i in range(3) for j in range(3) if board[i][j] == " "
    ]
    return random.choice(available_moves)


def restart_game():
    """
    Create an option for the player to restart the game against the computer.
    """
    while True:
        restart = input("Do you want to play again? (y/n): ").lower()
        if restart in ["y", "n"]:
            return restart == "y"
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")


def main():
    """
    Run all program functions.
    """
    print("Welcome to Noughts and Crosses")
    player_name = input("Please enter your name: ")
    welcome_message(player_name)

    while True:  # This loop allows restarting the game
        board = [
            [" " for _ in range(3)] for _ in range(3)
        ]  # Reset the board for each new game
        current_player = "X"

        while True:  # This loop runs a single game
            print_board(board)

            if current_player == "X":
                row, col = get_player_move(player_name)
            else:
                print("Computer's turn.")
                row, col = get_computer_move(board)

            if board[row][col] == " ":
                board[row][col] = (
                    X_COLOUR + "X" + Style.RESET_ALL
                    if current_player == "X"
                    else O_COLOUR + "O" + Style.RESET_ALL
                )
            else:
                if current_player == "X":
                    print("This spot is already taken. Please try again.")
                continue

            if check_win(board, current_player):
                print_board(board)
                if current_player == "X":
                    print(f"Congratulations, {player_name}! You win!")
                else:
                    print("You lose. Maybe next time.")
                break

            if check_draw(board):
                print_board(board)
                print("Draw, we all win, or everybody loses. Your choice.")
                break

            current_player = "O" if current_player == "X" else "X"

        if not restart_game():
            print("Thanks for playing, please come again.")
            break  # This break exits the main game loop


if __name__ == "__main__":
    main()
