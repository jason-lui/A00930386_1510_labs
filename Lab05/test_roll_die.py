from unittest import TestCase
from unittest.mock import patch
from lab05 import roll_die


class TestRoll_die(TestCase):

    def test_roll_true(self, mock_roll):
        number_of_rolls = 10
        number_of_sides = 10
        expected = True
        self.assertEqual(expected, roll_die(number_of_rolls, number_of_sides))

    @patch("random.randint", side_effect=[1, 2, 3, 4, 5, 6])
    def test_roll_0_0(self, mock_roll):
        number_of_rolls = 0
        number_of_sides = 0
        expected = 0
        self.assertEqual(expected, roll_die(number_of_rolls, number_of_sides))

    @patch("random.randint", side_effect=[1, 2, 3, 4, 5, 6])
    def test_roll_6_0(self, mock_roll):
        number_of_rolls = 6
        number_of_sides = 0
        expected = 0
        self.assertEqual(expected, roll_die(number_of_rolls, number_of_sides))

    @patch("random.randint", side_effect=[1, 2, 3, 4, 5, 6])
    def test_roll_0_6(self, mock_roll):
        number_of_rolls = 0
        number_of_sides = 6
        expected = 0
        self.assertEqual(expected, roll_die(number_of_rolls, number_of_sides))

    @patch("random.randint", side_effect=[1, 2, 3, 4, 5, 6])
    def test_roll_6_6(self, mock_roll):
        number_of_rolls = 6
        number_of_sides = 6
        expected = 21
        self.assertEqual(expected, roll_die(number_of_rolls, number_of_sides))
