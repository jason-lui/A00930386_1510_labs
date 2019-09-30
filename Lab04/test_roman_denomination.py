from unittest import TestCase
from roman_numbers import roman_denomination


class TestRoman_denomination(TestCase):

    def test_roman_denomination_1_to_1s(self):
        self.assertEqual('I', roman_denomination(1, 1))

    def test_roman_denomination_1_to_10s(self):
        self.assertEqual('', roman_denomination(1, 10))

    def test_roman_denomination_1_to_100s(self):
        self.assertEqual('', roman_denomination(1, 100))

    def test_roman_denomination_4_to_1s(self):
        self.assertEqual('IV', roman_denomination(4, 1))

    def test_roman_denomination_4_to_10s(self):
        self.assertEqual('', roman_denomination(4, 10))

    def test_roman_denomination_4_to_100s(self):
        self.assertEqual('', roman_denomination(4, 100))

    def test_roman_denomination_5_to_1s(self):
        self.assertEqual('V', roman_denomination(5, 1))

    def test_roman_denomination_5_to_10s(self):
        self.assertEqual('', roman_denomination(5, 10))

    def test_roman_denomination_5_to_100s(self):
        self.assertEqual('', roman_denomination(5, 100))

    def test_roman_denomination_9_to_1s(self):
        self.assertEqual('IX', roman_denomination(9, 1))

    def test_roman_denomination_9_to_10s(self):
        self.assertEqual('', roman_denomination(9, 10))

    def test_roman_denomination_9_to_100s(self):
        self.assertEqual('', roman_denomination(9, 100))

    def test_roman_denomination_10_to_1s(self):
        self.assertEqual('', roman_denomination(10, 1))

    def test_roman_denomination_10_to_10s(self):
        self.assertEqual('X', roman_denomination(10, 10))

    def test_roman_denomination_10_to_100s(self):
        self.assertEqual('', roman_denomination(10, 100))

    def test_roman_denomination_40_to_1s(self):
        self.assertEqual('', roman_denomination(40, 1))

    def test_roman_denomination_40_to_10s(self):
        self.assertEqual('XL', roman_denomination(40, 10))

    def test_roman_denomination_40_to_100s(self):
        self.assertEqual('', roman_denomination(40, 100))

    def test_roman_denomination_50_to_1s(self):
        self.assertEqual('', roman_denomination(50, 1))

    def test_roman_denomination_50_to_10s(self):
        self.assertEqual('L', roman_denomination(50, 10))

    def test_roman_denomination_50_to_100s(self):
        self.assertEqual('', roman_denomination(50, 100))

    def test_roman_denomination_60_to_1s(self):
        self.assertEqual('', roman_denomination(60, 1))

    def test_roman_denomination_60_to_10s(self):
        self.assertEqual('LX', roman_denomination(60, 10))

    def test_roman_denomination_60_to_100s(self):
        self.assertEqual('', roman_denomination(60, 100))

    def test_roman_denomination_90_to_1s(self):
        self.assertEqual('', roman_denomination(90, 1))

    def test_roman_denomination_90_to_10s(self):
        self.assertEqual('XC', roman_denomination(90, 10))

    def test_roman_denomination_90_to_100s(self):
        self.assertEqual('', roman_denomination(90, 100))

    def test_roman_denomination_100_to_1s(self):
        self.assertEqual('', roman_denomination(100, 1))

    def test_roman_denomination_100_to_10s(self):
        self.assertEqual('', roman_denomination(100, 10))

    def test_roman_denomination_100_to_100s(self):
        self.assertEqual('C', roman_denomination(100, 100))

    def test_roman_denomination_400_to_1s(self):
        self.assertEqual('', roman_denomination(400, 1))

    def test_roman_denomination_400_to_10s(self):
        self.assertEqual('', roman_denomination(400, 10))

    def test_roman_denomination_400_to_100s(self):
        self.assertEqual('CD', roman_denomination(400, 100))

    def test_roman_denomination_500_to_1s(self):
        self.assertEqual('', roman_denomination(500, 1))

    def test_roman_denomination_500_to_10s(self):
        self.assertEqual('', roman_denomination(500, 10))

    def test_roman_denomination_500_to_100s(self):
        self.assertEqual('D', roman_denomination(500, 100))

    def test_roman_denomination_600_to_1s(self):
        self.assertEqual('', roman_denomination(600, 1))

    def test_roman_denomination_600_to_10s(self):
        self.assertEqual('', roman_denomination(600, 10))

    def test_roman_denomination_600_to_100s(self):
        self.assertEqual('DC', roman_denomination(600, 100))

    def test_roman_denomination_900_to_1s(self):
        self.assertEqual('', roman_denomination(900, 1))

    def test_roman_denomination_900_to_10s(self):
        self.assertEqual('', roman_denomination(900, 10))

    def test_roman_denomination_900_to_100s(self):
        self.assertEqual('CM', roman_denomination(900, 100))

    def test_roman_denomination_10000_to_1s(self):
        self.assertEqual('', roman_denomination(10000, 1))

    def test_roman_denomination_10000_to_10s(self):
        self.assertEqual('', roman_denomination(10000, 10))

    def test_roman_denomination_10000_to_100s(self):
        self.assertEqual('', roman_denomination(10000, 100))

    def test_roman_denomination_3489_to_1s(self):
        self.assertEqual('IX', roman_denomination(3489, 1))

    def test_roman_denomination_3489_to_10s(self):
        self.assertEqual('LXXX', roman_denomination(3489, 10))

    def test_roman_denomination_3489_to_100s(self):
        self.assertEqual('CD', roman_denomination(3489, 100))
