import doctest


def game():
    """

    """
    board = make_board()

    char = make_character()
    found_exit = False
    while not found_exit:
        # Tell the user where they are
        direction = get_user_choice()
        valid_move = validate_move(board, char, direction)
        if valid_move:
            move_character(char, direction)
            found_exit = check_if_exit_reached(char)
        else:
            # Tell the user they can’t go in that direction
            print()
    # Print end of game stuff


def make_board() -> list:
    """
    Generate a 5x5 board.

    0 represents a vacant space, 1 represents an occupied space, 2 represents the exit
    :postcondition: a 5x5 board will be generated with the character at (0, 0) and the exit at (4, 4)
    :return: a list of lists of ints representing a 5x5 board
    """
    board = [[0] * 5 for i in range(5)]
    board[-1][-1] += 2
    return board


def print_board(board: list):
    """
    Print the board.

    :param board: a list of lists
    :precondition: board must be a list of lists of int representing the board
    :postcondition: the board will be printed as a 2D array
    """
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print('')


def make_character() -> dict:
    """
    Create a dictionary that stores a tuple representing the character's location in the maze.

    :postcondition: a character containing (0, 0) will be created
    :return: a dictionary containing the location (0, 0) of the character
    """
    char_info = {'coords': (0, 0)}
    return char_info


def get_user_choice() -> tuple:
    """
    Show the user the available moves and get the user's movement direction

    :postcondition: the user's choice as a tuple containing coords of an xy-plane
    :return: the user's choice as a tuple
    """
    print("""
    Where would you like to move?
    1. North
    2. East
    3. South
    4. West""")
    choice = input("Enter your move (1-4): ")
    move_coords = {'1': (0, 1), '2': (1, 0), '3': (0, -1), '4': (-1, 0)}
    return move_coords[choice]


def validate_move(board: list, character: dict, move: tuple) -> bool:
    """
    Determine if a move is valid.

    :param board: a list of lists
    :param character: a dictionary
    :param move: a tuple
    :precondition: board must be a list of lists of int representing the board
    :precondition: character must be a dictionary containing the character's coordinates
    :precondition: direction must be a tuple representing a direction of movement
    :postcondition: the move will be validated
    :return: True or False depending on whether the move is valid
    """
    x = character['coords'][0] + move[0]
    y = character['coords'][1] + move[1]
    return True if (x > len(board)) or (y > len(board[1])) else False


def move_character(character: dict, move: tuple) -> dict:
    """
    Move a character 1 space on the board.

    :param character: a dictionary
    :param move: a string
    :precondition: character must be a dictionary containing the character's coordinates
    :precondition: move must be a string representing a cardinal direction
    :return: a dictionary containing the updated coordinates
    """
    character['coords'][0] += move[0]
    character['coords'][1] += move[1]
    return character


def check_if_exit_reached(character: dict) -> bool:
    """
    Determine if the character is at the exit

    :param character: a dictionary
    :precondition: character must be a dictionary containing the character's coordinates
    :return: True or False depending on the character's location
    """
    return True if character['coords'] == (4, 4) else False


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    doctest.testmod()

print_board([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]])