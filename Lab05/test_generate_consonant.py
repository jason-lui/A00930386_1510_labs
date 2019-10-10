from unittest import TestCase
from unittest.mock import patch
from lab05 import generate_consonant


class TestGenerate_consonant(TestCase):

    @patch("random.choice", return_value=98)
    def test_generate_vowel_b(self, mock_output):
        expected_letter = "b"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=99)
    def test_generate_vowel_c(self, mock_output):
        expected_letter = "c"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=100)
    def test_generate_vowel_d(self, mock_output):
        expected_letter = "d"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=102)
    def test_generate_vowel_f(self, mock_output):
        expected_letter = "f"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=103)
    def test_generate_vowel_g(self, mock_output):
        expected_letter = "g"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=104)
    def test_generate_vowel_h(self, mock_output):
        expected_letter = "h"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=106)
    def test_generate_vowel_j(self, mock_output):
        expected_letter = "j"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=107)
    def test_generate_vowel_k(self, mock_output):
        expected_letter = "k"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=108)
    def test_generate_vowel_l(self, mock_output):
        expected_letter = "l"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=109)
    def test_generate_vowel_m(self, mock_output):
        expected_letter = "m"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=110)
    def test_generate_vowel_n(self, mock_output):
        expected_letter = "n"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=112)
    def test_generate_vowel_p(self, mock_output):
        expected_letter = "p"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=113)
    def test_generate_vowel_q(self, mock_output):
        expected_letter = "q"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=114)
    def test_generate_vowel_r(self, mock_output):
        expected_letter = "r"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=115)
    def test_generate_vowel_s(self, mock_output):
        expected_letter = "s"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=116)
    def test_generate_vowel_t(self, mock_output):
        expected_letter = "t"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=118)
    def test_generate_vowel_v(self, mock_output):
        expected_letter = "v"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=119)
    def test_generate_vowel_w(self, mock_output):
        expected_letter = "w"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=120)
    def test_generate_vowel_x(self, mock_output):
        expected_letter = "x"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=121)
    def test_generate_vowel_y(self, mock_output):
        expected_letter = "y"
        self.assertEqual(expected_letter, generate_consonant())

    @patch("random.choice", return_value=122)
    def test_generate_vowel_z(self, mock_output):
        expected_letter = "z"
        self.assertEqual(expected_letter, generate_consonant())
