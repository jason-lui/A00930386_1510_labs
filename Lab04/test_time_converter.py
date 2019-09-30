from unittest import TestCase
from time_calculator import time_converter


class TestTime_converter(TestCase):

    def test_time_converter_0_to_seconds(self):
        self.assertEqual(0, time_converter(0, "seconds"))

    def test_time_converter_0_to_minutes(self):
        self.assertEqual(0, time_converter(0, "minutes"))

    def test_time_converter_0_to_hours(self):
        self.assertEqual(0, time_converter(0, "hours"))

    def test_time_converter_0_to_days(self):
        self.assertEqual(0, time_converter(0, "days"))

    def test_time_converter_1_to_seconds(self):
        self.assertEqual(1, time_converter(1, "seconds"))

    def test_time_converter_1_to_minutes(self):
        self.assertEqual(0, time_converter(1, "minutes"))

    def test_time_converter_1_to_hours(self):
        self.assertEqual(0, time_converter(1, "hours"))

    def test_time_converter_1_to_days(self):
        self.assertEqual(0, time_converter(1, "days"))

    def test_time_converter_60_to_seconds(self):
        self.assertEqual(0, time_converter(60, "seconds"))

    def test_time_converter_60_to_minutes(self):
        self.assertEqual(1, time_converter(60, "minutes"))

    def test_time_converter_60_to_hours(self):
        self.assertEqual(0, time_converter(60, "hours"))

    def test_time_converter_60_to_days(self):
        self.assertEqual(0, time_converter(60, "days"))

    def test_time_converter_3600_to_seconds(self):
        self.assertEqual(0, time_converter(3600, "seconds"))

    def test_time_converter_3600_to_minutes(self):
        self.assertEqual(0, time_converter(3600, "minutes"))

    def test_time_converter_3600_to_hours(self):
        self.assertEqual(1, time_converter(3600, "hours"))

    def test_time_converter_3600_to_days(self):
        self.assertEqual(0, time_converter(3600, "days"))

    def test_time_converter_86400_to_seconds(self):
        self.assertEqual(0, time_converter(86400, "seconds"))

    def test_time_converter_86400_to_minutes(self):
        self.assertEqual(0, time_converter(86400, "minutes"))

    def test_time_converter_86400_to_hours(self):
        self.assertEqual(0, time_converter(86400, "hours"))

    def test_time_converter_86400_to_days(self):
        self.assertEqual(1, time_converter(86400, "days"))

    def test_time_converter_100000_to_seconds(self):
        self.assertEqual(40, time_converter(100000, "seconds"))

    def test_time_converter_100000_to_minutes(self):
        self.assertEqual(46, time_converter(100000, "minutes"))

    def test_time_converter_100000_to_hours(self):
        self.assertEqual(3, time_converter(100000, "hours"))

    def test_time_converter_100000_to_days(self):
        self.assertEqual(1, time_converter(100000, "days"))
