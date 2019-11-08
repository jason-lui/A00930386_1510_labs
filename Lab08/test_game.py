from unittest import TestCase
from unittest.mock import patch
from maze import game
import io


class TestGame(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=['2', '2', '2', '2', '3', '3', '3', '3'])
    def test_game_valid_path(self, mock_input, mock_output):
        expected = """1 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 1 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 0 1 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 0 0 0
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 1
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

It took you 8 moves to reach the exit.
"""
        game()
        self.assertEqual(expected, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=['1', '4', '2', '2', '2', '2', '2', '4', '3', '3', '3', '3', '3', '2'])
    def test_game_invalid_path(self, mock_input, mock_output):
        expected = """1 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

You can't go in that direction!
1 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

You can't go in that direction!
1 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 1 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 0 1 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

You can't go in that direction!
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 0 1 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 0 0 0
0 0 0 1 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 0 0 0
0 0 0 0 0
0 0 0 1 0
0 0 0 0 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 0
0 0 0 0 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

You can't go in that direction!
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 2
Where would you like to move?
1. North, 2. East, 3. South, 4. West

It took you 10 moves to reach the exit.
"""
        game()
        self.assertEqual(expected, mock_output.getvalue())
