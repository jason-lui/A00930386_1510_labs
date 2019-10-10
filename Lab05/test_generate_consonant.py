from unittest import TestCase
from unittest.mock import patch
from lab05 import generate_consonant


class TestGenerate_consonant(TestCase):

    @patch("random.choice", return_value=98)
    def test_generate_vowel_b(self, mock_output):
        self.assertEqual("b", generate_consonant())

    @patch("random.choice", return_value=99)
    def test_generate_vowel_c(self, mock_output):
        self.assertEqual("c", generate_consonant())

    @patch("random.choice", return_value=100)
    def test_generate_vowel_d(self, mock_output):
        self.assertEqual("d", generate_consonant())

    @patch("random.choice", return_value=102)
    def test_generate_vowel_f(self, mock_output):
        self.assertEqual("f", generate_consonant())

    @patch("random.choice", return_value=103)
    def test_generate_vowel_g(self, mock_output):
        self.assertEqual("g", generate_consonant())

    @patch("random.choice", return_value=104)
    def test_generate_vowel_h(self, mock_output):
        self.assertEqual("h", generate_consonant())

    @patch("random.choice", return_value=106)
    def test_generate_vowel_j(self, mock_output):
        self.assertEqual("j", generate_consonant())

    @patch("random.choice", return_value=107)
    def test_generate_vowel_k(self, mock_output):
        self.assertEqual("k", generate_consonant())

    @patch("random.choice", return_value=108)
    def test_generate_vowel_l(self, mock_output):
        self.assertEqual("l", generate_consonant())

    @patch("random.choice", return_value=109)
    def test_generate_vowel_m(self, mock_output):
        self.assertEqual("m", generate_consonant())

    @patch("random.choice", return_value=110)
    def test_generate_vowel_n(self, mock_output):
        self.assertEqual("n", generate_consonant())

    @patch("random.choice", return_value=112)
    def test_generate_vowel_p(self, mock_output):
        self.assertEqual("p", generate_consonant())

    @patch("random.choice", return_value=113)
    def test_generate_vowel_q(self, mock_output):
        self.assertEqual("q", generate_consonant())

    @patch("random.choice", return_value=114)
    def test_generate_vowel_r(self, mock_output):
        self.assertEqual("r", generate_consonant())

    @patch("random.choice", return_value=115)
    def test_generate_vowel_s(self, mock_output):
        self.assertEqual("s", generate_consonant())

    @patch("random.choice", return_value=116)
    def test_generate_vowel_t(self, mock_output):
        self.assertEqual("t", generate_consonant())

    @patch("random.choice", return_value=118)
    def test_generate_vowel_v(self, mock_output):
        self.assertEqual("v", generate_consonant())

    @patch("random.choice", return_value=119)
    def test_generate_vowel_w(self, mock_output):
        self.assertEqual("w", generate_consonant())

    @patch("random.choice", return_value=120)
    def test_generate_vowel_x(self, mock_output):
        self.assertEqual("x", generate_consonant())

    @patch("random.choice", return_value=121)
    def test_generate_vowel_y(self, mock_output):
        self.assertEqual("y", generate_consonant())

    @patch("random.choice", return_value=122)
    def test_generate_vowel_z(self, mock_output):
        self.assertEqual("z", generate_consonant())
