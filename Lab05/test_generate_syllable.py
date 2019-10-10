from unittest import TestCase
from unittest.mock import patch
from lab05 import generate_syllable

vowels = ["a", "e", "i", "o", "u", "y"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


class TestGenerate_syllable(TestCase):

    def test_generate_syllable_true(self):
        expected = True
        syllable = generate_syllable()
        self.assertEqual(expected, (syllable[0] in consonants and
                                    syllable[1] in vowels))

    @patch("random.choice", side_effect=[98, 97])
    def test_generate_syllable_ba(self, mock_letter):
        expected = "ba"
        self.assertEqual(expected, generate_syllable())

    @patch("random.choice", side_effect=[122, 97])
    def test_generate_syllable_za(self, mock_letter):
        expected = "za"
        self.assertEqual(expected, generate_syllable())

    @patch("random.choice", side_effect=[122, 121])
    def test_generate_syllable_zy(self, mock_letter):
        expected = "zy"
        self.assertEqual(expected, generate_syllable())

    @patch("random.choice", side_effect=[121, 121])
    def test_generate_syllable_yy(self, mock_letter):
        expected = "yy"
        self.assertEqual(expected, generate_syllable())
