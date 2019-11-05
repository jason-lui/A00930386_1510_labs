from unittest import TestCase
from unittest.mock import patch
from maze import print_board
import io


class TestPrint_board(TestCase):

    # def print_board(board: list):
    #     """
    #     Print the board.
    #
    #     :param board: a list of lists
    #     :precondition: board must be a list of lists of int representing the board
    #     :postcondition: the board will be printed as a 2D array
    #
    #     >>> print_board([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,2]])
    #     1 0 0 0 0
    #     0 0 0 0 0
    #     0 0 0 0 0
    #     0 0 0 0 0
    #     0 0 0 0 2
    #     >>> print_board([[1,0,0], [0,0,0], [0,0,2]])
    #     1 0 0
    #     0 0 0
    #     0 0 2
    #     """
    #     for row in board:
    #         row_str = ""
    #         for cell in row:
    #             row_str += str(cell) + ' '
    #         print(row_str.strip())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_board_start_0_0_end_4_4_in_5x5_board(self, mock_output):
        test_board = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]
        expected = "1 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 2\n"
        print_board(test_board)
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_board_start_0_0_end_2_2_in_3x3_board(self, mock_output):
        test_board = [[1, 0, 0], [0, 0, 0], [0, 0, 2]]
        expected = "1 0 0\n0 0 0\n0 0 2\n"
        print_board(test_board)
        self.assertEqual(expected, mock_output.getvalue())
