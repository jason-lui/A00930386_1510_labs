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
    char_info = {'Coordinates': (0, 0)}
    return char_info


def get_user_choice() -> str:
    """
    Show the user the available moves and get the user's choice

    :postcondition: the user's choice will be returned as a string
    :return: the user's choice as a string
    """
    print("""
    Where would you like to move?
    1. North
    2. East
    3. South
    4. West""")
    choice = input("Enter your move (1-4): ")
    return choice


def validate_move(board, character, direction):
    """

    :param board:
    :param character:
    :param direction:
    :return:
    """


def move_character(character: dict) -> dict:
    """

    :param character:
    :return:
    """


def check_if_exit_reached(character: dict) -> bool:
    """

    :param character:
    :return:
    """


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    doctest.testmod()
