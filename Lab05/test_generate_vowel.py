from unittest import TestCase
from unittest.mock import patch
from lab05 import generate_vowel


class TestGenerate_vowel(TestCase):

    @patch("random.choice", return_value=97)
    def test_generate_vowel_a(self, mock_output):
        self.assertEqual("a", generate_vowel())

    @patch("random.choice", return_value=101)
    def test_generate_vowel_e(self, mock_output):
        self.assertEqual("e", generate_vowel())

    @patch("random.choice", return_value=105)
    def test_generate_vowel_i(self, mock_output):
        self.assertEqual("i", generate_vowel())

    @patch("random.choice", return_value=111)
    def test_generate_vowel_o(self, mock_output):
        self.assertEqual("o", generate_vowel())

    @patch("random.choice", return_value=117)
    def test_generate_vowel_u(self, mock_output):
        self.assertEqual("u", generate_vowel())

    @patch("random.choice", return_value=121)
    def test_generate_vowel_y(self, mock_output):
        self.assertEqual("y", generate_vowel())
