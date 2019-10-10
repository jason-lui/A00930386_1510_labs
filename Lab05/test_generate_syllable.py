from unittest import TestCase
from unittest.mock import patch
from lab05 import generate_syllable


class TestGenerate_syllable(TestCase):

    @patch("random.choice", side_effect=[98, 97])
    def test_generate_syllable_ba(self, mock_letter):
        self.assertEqual("ba", generate_syllable())

    @patch("random.choice", side_effect=[122, 97])
    def test_generate_syllable_za(self, mock_letter):
        self.assertEqual("za", generate_syllable())

    @patch("random.choice", side_effect=[122, 121])
    def test_generate_syllable_zy(self, mock_letter):
        self.assertEqual("zy", generate_syllable())

    @patch("random.choice", side_effect=[121, 121])
    def test_generate_syllable_yy(self, mock_letter):
        self.assertEqual("yy", generate_syllable())
