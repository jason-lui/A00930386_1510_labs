from unittest import TestCase
from lab05 import generate_consonant

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


class TestGenerate_consonant(TestCase):

    def test_generate_vowel_true(self):
        self.assertTrue(generate_consonant() in consonants)
