import io
from unittest import TestCase
from unittest.mock import patch
from time_calculator import time_calculator


class TestTime_calculator(TestCase):

    @patch('sys.stdout', new_callable = io.StringIO)
    def test_time_calculator_0(self, mock_stdout):
        number = 0
        expected_output = "0 0 0 0\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_1(self, mock_stdout):
        number = 1
        expected_output = "0 0 0 1\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_60(self, mock_stdout):
        number = 60
        expected_output = "0 0 1 0\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_61(self, mock_stdout):
        number = 61
        expected_output = "0 0 1 1\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_3600(self, mock_stdout):
        number = 3600
        expected_output = "0 1 0 0\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_3601(self, mock_stdout):
        number = 3601
        expected_output = "0 1 0 1\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_3661(self, mock_stdout):
        number = 3661
        expected_output = "0 1 1 1\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_86400(self, mock_stdout):
        number = 86400
        expected_output = "1 0 0 0\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_86401(self, mock_stdout):
        number = 86401
        expected_output = "1 0 0 1\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_86460(self, mock_stdout):
        number = 86460
        expected_output = "1 0 1 0\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_90000(self, mock_stdout):
        number = 90000
        expected_output = "1 1 0 0\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_90001(self, mock_stdout):
        number = 90001
        expected_output = "1 1 0 1\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_90060(self, mock_stdout):
        number = 90060
        expected_output = "1 1 1 0\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_90061(self, mock_stdout):
        number = 90061
        expected_output = "1 1 1 1\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_calculator_100000(self, mock_stdout):
        number = 100000
        expected_output = "1 3 46 40\n"
        time_calculator(number)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
