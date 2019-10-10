from unittest import TestCase
from unittest.mock import patch
from lab05 import generate_vowel


class TestGenerate_vowel(TestCase):

    @patch("random.choice", return_value=97)
    def test_generate_vowel_a(self, mock_output):
        expected_letter = "a"
        self.assertEqual(expected_letter, generate_vowel())

    @patch("random.choice", return_value=101)
    def test_generate_vowel_e(self, mock_output):
        expected_letter = "e"
        self.assertEqual(expected_letter, generate_vowel())

    @patch("random.choice", return_value=105)
    def test_generate_vowel_i(self, mock_output):
        expected_letter = "i"
        self.assertEqual(expected_letter, generate_vowel())

    @patch("random.choice", return_value=111)
    def test_generate_vowel_o(self, mock_output):
        expected_letter = "o"
        self.assertEqual(expected_letter, generate_vowel())

    @patch("random.choice", return_value=117)
    def test_generate_vowel_u(self, mock_output):
        expected_letter = "u"
        self.assertEqual(expected_letter, generate_vowel())

    @patch("random.choice", return_value=121)
    def test_generate_vowel_y(self, mock_output):
        expected_letter = "y"
        self.assertEqual(expected_letter, generate_vowel())
