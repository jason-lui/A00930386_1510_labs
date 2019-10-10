from unittest import TestCase
from lab05 import generate_vowel

vowels = ["a", "e", "i", "o", "u", "y"]


class TestGenerate_vowel(TestCase):

    def test_generate_vowel(self):
        self.assertTrue(generate_vowel() in vowels)
