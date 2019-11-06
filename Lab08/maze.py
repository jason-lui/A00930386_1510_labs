import doctest


def game():
    """
    Run the maze game until an exit has been found.
    """
    # Initial game state
    char = make_character()
    game_board = update_board(char)
    found_exit = False
    number_of_moves = 0

    # Infinite loop for character movement
    while not found_exit:
        # Tell the user where they are
        print_board(game_board)

        # Get user input and validate input
        direction = get_user_choice()
        valid_move = validate_move(game_board, char, direction)

        if valid_move:
            # Move character and validate exit conditions
            move_character(char, direction)
            found_exit = check_if_exit_reached(char)
            game_board = update_board(char)
            number_of_moves += 1
        else:
            print("You can't go in that direction!")
    print(f"It took you {number_of_moves} moves to reach the exit.")


def make_board() -> list:
    """
    Generate a 5x5 board.

    0 represents a vacant space, 1 represents an occupied space, 2 represents the exit
    :postcondition: a 5x5 board will be generated with the exit at (4, 4)
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

    >>> print_board([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,2]])
    1 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 2
    >>> print_board([[1,0,0], [0,0,0], [0,0,2]])
    1 0 0
    0 0 0
    0 0 2
    """
    for row in board:
        row_str = ""
        for cell in row:
            row_str += str(cell) + ' '
        print(row_str.strip())


def update_board(character: dict) -> list:
    """
    Update the board with the character's coordinates.

    :param character: a dictionary
    :precondition: character must be a dictionary containing the character's coordinates
    :precondition: board must be a list of lists of int representing the board
    :postcondition: the board will be updated with the character's current position
    :return: the updated board as a list of lists

    >>> update_board({'coords': (0, 0)})
    [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]
    >>> update_board({'coords': (1, 1)})
    [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]
    """
    board = make_board()
    x, y = character['coords'][0], character['coords'][1]
    board[y][x] = 1

    return board


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
    move_coords = {'1': (0, -1), '2': (1, 0), '3': (0, 1), '4': (-1, 0)}

    print("Where would you like to move?")
    print("1. North, 2. East, 3. South, 4. West")
    choice = input("Enter your move (1-4): ")
    while choice not in move_coords.keys():
        print("That is not a valid move.")
        choice = input("Choose a number between 1 and 4: ")
    print('')
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

    >>> validate_move([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,2]], {'coords': (0, 0)}, (0, -1))
    False
    >>> validate_move([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,2]], {'coords': (0, 0)}, (0, 1))
    True
    """
    x = character['coords'][0] + move[0]
    y = character['coords'][1] + move[1]
    return True if ((0 <= x <= len(board) - 1) and (0 <= y <= len(board[1]) - 1)) else False


def move_character(character: dict, move: tuple) -> dict:
    """
    Move a character 1 space on the board.

    :param character: a dictionary
    :param move: a string
    :precondition: character must be a dictionary containing the character's coordinates
    :precondition: move must be a string representing a cardinal direction
    :return: a dictionary containing the updated coordinates

    >>> move_character({'coords': (0, 0)}, (0, 1))
    {'coords': (0, 1)}
    >>> move_character({'coords': (0, 0)}, (1, 0))
    {'coords': (1, 0)}
    >>> move_character({'coords': (1, 1)}, (0, -1))
    {'coords': (1, 0)}
    >>> move_character({'coords': (1, 1)}, (-1, 0))
    {'coords': (0, 1)}
    """
    x = character['coords'][0] + move[0]
    y = character['coords'][1] + move[1]
    character['coords'] = (x, y)
    return character


def check_if_exit_reached(character: dict) -> bool:
    """
    Determine if the character is at the exit

    :param character: a dictionary
    :precondition: character must be a dictionary containing the character's coordinates
    :return: True or False depending on the character's location

    >>> check_if_exit_reached({'coords': (0, 0)})
    False
    >>> check_if_exit_reached({'coords': (4, 4)})
    True
    """
    return True if character['coords'] == (4, 4) else False


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
    doctest.testmod()
