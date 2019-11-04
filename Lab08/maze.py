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
            move_character(char)
            found_exit = check_if_exit_reached(char)
        else:
            # Tell the user they can’t go in that direction
            print()
    # Print end of game stuff


def make_board() -> list[list[int]]:
    """

    :return:
    """


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


def validate_move(board, character, direction):
    """

    :param board:
    :param character:
    :param direction:
    :return:
    """


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
    :precondition: character must be a dictionary
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
