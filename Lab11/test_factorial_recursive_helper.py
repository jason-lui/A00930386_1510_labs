from unittest import TestCase
from lab11 import factorial_recursive_helper


class TestFactorial_recursive_helper(TestCase):

    def test_factorial_recursive_helper_neg1(self):
        num = -1
        expected = RecursionError
        self.assertRaises(expected, factorial_recursive_helper, num)

    def test_factorial_recursive_helper_0(self):
        num = 0
        expected = RecursionError
        self.assertRaises(expected, factorial_recursive_helper, num)

    def test_factorial_recursive_helper_1(self):
        num = 1
        expected = 1
        self.assertEqual(expected, factorial_recursive_helper(num))

    def test_factorial_recursive_helper_100(self):
        num = 50
        expected = 30414093201713378043612608166064768844377641568960512000000000000
        self.assertEqual(expected, factorial_recursive_helper(num))
