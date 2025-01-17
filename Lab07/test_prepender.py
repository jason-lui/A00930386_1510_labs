from unittest import TestCase
from midterm import prepender


class TestPrepender(TestCase):

    def test_prepender_empty_and_empty(self):
        test_list = []
        test_prefix = ""
        expected = []
        prepender(test_list, test_prefix)
        self.assertEqual(expected, test_list)

    def test_prepender_empty_and_not_empty(self):
        test_list = []
        test_prefix = "Python"
        expected = []
        prepender(test_list, test_prefix)
        self.assertEqual(expected, test_list)

    def test_prepender_1_and_empty(self):
        test_list = ["Python"]
        test_prefix = ""
        expected = ["Python"]
        prepender(test_list, test_prefix)
        self.assertEqual(expected, test_list)

    def test_prepender_1_and_not_empty(self):
        test_list = ["Python"]
        test_prefix = "I love "
        expected = ["I love Python"]
        prepender(test_list, test_prefix)
        self.assertEqual(expected, test_list)

    def test_prepender_multiple_and_empty(self):
        test_list = ["Python", "is", "better", "than", "JavaScript"]
        test_prefix = ""
        expected = ["Python", "is", "better", "than", "JavaScript"]
        prepender(test_list, test_prefix)
        self.assertEqual(expected, test_list)

    def test_prepender_multiple_and_not_empty(self):
        test_list = ["Python", "is", "better", "than", "JavaScript"]
        test_prefix = "Umm... "
        expected = ["Umm... Python", "Umm... is", "Umm... better",
                    "Umm... than", "Umm... JavaScript"]
        prepender(test_list, test_prefix)
        self.assertEqual(expected, test_list)

    def test_prepender_numbers(self):
        test_list = [0, 1, 2, 3]
        test_prefix = 2
        expected = [2, 3, 4, 5]
        prepender(test_list, test_prefix)
        self.assertEqual(expected, test_list)

    def test_prepender_list_of_lists(self):
        test_list = [["Python", "is"], ["better", "than"], ["JavaScript"]]
        test_prefix = ["Umm... "]
        expected = [["Umm... ", "Python", "is"], ["Umm... ", "better",
                    "than"], ["Umm... ", "JavaScript"]]
        prepender(test_list, test_prefix)
        self.assertEqual(expected, test_list)
