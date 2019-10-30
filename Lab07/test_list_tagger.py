from unittest import TestCase
from midterm import list_tagger


class TestList_tagger(TestCase):

    def test_list_tagger_empty(self):
        test_list = []
        expected = [0]
        self.assertEqual(expected, list_tagger(test_list))

    def test_list_tagger_1(self):
        test_list = ["banana"]
        expected = [1, "banana"]
        self.assertEqual(expected, list_tagger(test_list))

    def test_list_tagger_3(self):
        test_list = [1, 2, 3]
        expected = [3, 1, 2, 3]
        self.assertEqual(expected, list_tagger(test_list))
