from unittest import TestCase
from unittest.mock import patch
from lab05 import generate_consonant

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


class TestGenerate_consonant(TestCase):

    def test_generate_vowel_true(self):
        expected = True
        self.assertEqual(expected, generate_consonant() in consonants)

    @patch("random.choice", return_value=98)
    def test_generate_vowel_b(self, mock_output):
        expected = "b"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=99)
    def test_generate_vowel_c(self, mock_output):
        expected = "c"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=100)
    def test_generate_vowel_d(self, mock_output):
        expected = "d"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=102)
    def test_generate_vowel_f(self, mock_output):
        expected = "f"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=103)
    def test_generate_vowel_g(self, mock_output):
        expected = "g"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=104)
    def test_generate_vowel_h(self, mock_output):
        expected = "h"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=106)
    def test_generate_vowel_j(self, mock_output):
        expected = "j"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=107)
    def test_generate_vowel_k(self, mock_output):
        expected = "k"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=108)
    def test_generate_vowel_l(self, mock_output):
        expected = "l"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=109)
    def test_generate_vowel_m(self, mock_output):
        expected = "m"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=110)
    def test_generate_vowel_n(self, mock_output):
        expected = "n"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=112)
    def test_generate_vowel_p(self, mock_output):
        expected = "p"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=113)
    def test_generate_vowel_q(self, mock_output):
        expected = "q"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=114)
    def test_generate_vowel_r(self, mock_output):
        expected = "r"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=115)
    def test_generate_vowel_s(self, mock_output):
        expected = "s"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=116)
    def test_generate_vowel_t(self, mock_output):
        expected = "t"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=118)
    def test_generate_vowel_v(self, mock_output):
        expected = "v"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=119)
    def test_generate_vowel_w(self, mock_output):
        expected = "w"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=120)
    def test_generate_vowel_x(self, mock_output):
        expected = "x"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=121)
    def test_generate_vowel_y(self, mock_output):
        expected = "y"
        self.assertEqual(expected, generate_consonant())

    @patch("random.choice", return_value=122)
    def test_generate_vowel_z(self, mock_output):
        expected = "z"
        self.assertEqual(expected, generate_consonant())
