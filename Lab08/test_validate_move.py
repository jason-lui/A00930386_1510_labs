from unittest import TestCase
from maze import validate_move


class TestValidate_move(TestCase):

    # def validate_move(board: list, character: dict, move: tuple) -> bool:
    #     """
    #     Determine if a move is valid.
    #
    #     :param board: a list of lists
    #     :param character: a dictionary
    #     :param move: a tuple
    #     :precondition: board must be a list of lists of int representing the board
    #     :precondition: character must be a dictionary containing the character's coordinates
    #     :precondition: direction must be a tuple representing a direction of movement
    #     :postcondition: the move will be validated
    #     :return: True or False depending on whether the move is valid
    #     """
    #     x = character['coords'][0] + move[0]
    #     y = character['coords'][1] + move[1]
    #     return True if ((0 <= x <= len(board) - 1) and (0 <= y <= len(board[1]) - 1)) else False

    def test_validate_move(self):
        self.fail()
