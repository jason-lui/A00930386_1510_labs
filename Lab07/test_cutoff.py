from unittest import TestCase
from midterm import cutoff


class TestCutoff(TestCase):

    def test_cutoff_empty_and_0(self):
        test_list = []
        test_cutoff = 0
        expected = 0
        self.assertEqual(expected, cutoff(test_list, test_cutoff))

    def test_cutoff_empty_and_5(self):
        test_list = []
        test_cutoff = 5
        expected = 0
        self.assertEqual(expected, cutoff(test_list, test_cutoff))

    def test_cutoff_0_and_0(self):
        test_list = [0]
        test_cutoff = 0
        self.assertRaises(ZeroDivisionError, cutoff, test_list, test_cutoff)

    def test_cutoff_0_and_5(self):
        test_list = [0]
        test_cutoff = 5
        expected = 0
        self.assertEqual(expected, cutoff(test_list, test_cutoff))

    def test_cutoff_2_and_2(self):
        test_list = [2]
        test_cutoff = 2
        expected = 1
        self.assertEqual(expected, cutoff(test_list, test_cutoff))

    def test_cutoff_2_and_4(self):
        test_list = [2]
        test_cutoff = 4
        expected = 0
        self.assertEqual(expected, cutoff(test_list, test_cutoff))

    def test_cutoff_5_pos_and_0(self):
        test_list = [1, 2, 3, 4, 5]
        test_cutoff = 0
        self.assertRaises(ZeroDivisionError, cutoff, test_list, test_cutoff)

    def test_cutoff_5_pos_and_not_0(self):
        test_list = [1, 2, 3, 4, 5]
        test_cutoff = 3
        expected = 1
        self.assertEqual(expected, cutoff(test_list, test_cutoff))

    def test_cutoff_5x2_and_2(self):
        test_list = [2, 2, 2, 2, 2]
        test_cutoff = 2
        expected = 5
        self.assertEqual(expected, cutoff(test_list, test_cutoff))

    def test_cutoff_5x2_and_3(self):
        test_list = [2, 2, 2, 2, 2]
        test_cutoff = 3
        expected = 0
        self.assertEqual(expected, cutoff(test_list, test_cutoff))

    def test_cutoff_all_divisible(self):
        test_list = [3, 6, 9, 12, 15]
        test_cutoff = 3
        expected = 5
        self.assertEqual(expected, cutoff(test_list, test_cutoff))

    def test_cutoff_negatives(self):
        test_list = [-1, -2, -3, -4, -5, -6]
        test_cutoff = -2
        expected = 3
        self.assertEqual(expected, cutoff(test_list, test_cutoff))
