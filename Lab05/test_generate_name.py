from unittest import TestCase
from unittest.mock import patch
from lab05 import generate_name


class TestGenerate_name(TestCase):

    @patch("random.choice", side_effect=[98, 97, 100, 101, 104, 105])
    def test_generate_name_1(self, mock_letter):
        syllables = 1
        expected_name = "Ba"
        self.assertEqual(expected_name, generate_name(syllables))

    @patch("random.choice", side_effect=[98, 97, 100, 101, 104, 105])
    def test_generate_name_2(self, mock_letter):
        syllables = 2
        expected_name = "Bade"
        self.assertEqual(expected_name, generate_name(syllables))

    @patch("random.choice", side_effect=[98, 97, 100, 101, 104, 105])
    def test_generate_name_3(self, mock_letter):
        syllables = 3
        expected_name = "Badehi"
        self.assertEqual(expected_name, generate_name(syllables))




    # def test_generate_name_2(self):
    # def test_generate_name_3(self):