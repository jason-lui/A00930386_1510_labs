from unittest import TestCase
from unittest.mock import patch
from lab05 import generate_vowel

vowels = ["a", "e", "i", "o", "u", "y"]


class TestGenerate_vowel(TestCase):

    def test_generate_vowel(self):
        expected = True
        self.assertEqual(expected, generate_vowel() in vowels)

    @patch("random.choice", return_value=97)
    def test_generate_vowel_a(self, mock_output):
        expected = "a"
        self.assertEqual(expected, generate_vowel())

    @patch("random.choice", return_value=101)
    def test_generate_vowel_e(self, mock_output):
        expected = "e"
        self.assertEqual(expected, generate_vowel())

    @patch("random.choice", return_value=105)
    def test_generate_vowel_i(self, mock_output):
        expected = "i"
        self.assertEqual(expected, generate_vowel())

    @patch("random.choice", return_value=111)
    def test_generate_vowel_o(self, mock_output):
        expected = "o"
        self.assertEqual(expected, generate_vowel())

    @patch("random.choice", return_value=117)
    def test_generate_vowel_u(self, mock_output):
        expected = "u"
        self.assertEqual(expected, generate_vowel())

    @patch("random.choice", return_value=121)
    def test_generate_vowel_y(self, mock_output):
        expected = "y"
        self.assertEqual(expected, generate_vowel())
