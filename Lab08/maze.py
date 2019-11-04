import doctest


def game():
    """

    """
    board = make_board()

    character = make_character()
    found_exit = False
    while not found_exit:
        # Tell the user where they are
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character()
            found_exit = check_if_exit_reached()
        else:
            # Tell the user they can’t go in that direction
            print()
    # Print end of game stuff


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    doctest.testmod()