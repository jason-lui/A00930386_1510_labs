from unittest import TestCase
from unittest.mock import patch
from lab05 import generate_syllable


class TestGenerate_syllable(TestCase):

    @patch("random.choice", side_effect=[98, 97])
    def test_generate_syllable_ba(self, mock_letter):
        expected_syllable = "ba"
        self.assertEqual(expected_syllable, generate_syllable())

    @patch("random.choice", side_effect=[122, 97])
    def test_generate_syllable_za(self, mock_letter):
        expected_syllable = "za"
        self.assertEqual(expected_syllable, generate_syllable())

    @patch("random.choice", side_effect=[122, 121])
    def test_generate_syllable_zy(self, mock_letter):
        expected_syllable = "zy"
        self.assertEqual(expected_syllable, generate_syllable())

    @patch("random.choice", side_effect=[121, 121])
    def test_generate_syllable_yy(self, mock_letter):
        expected_syllable = "yy"
        self.assertEqual(expected_syllable, generate_syllable())
