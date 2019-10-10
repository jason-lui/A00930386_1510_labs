from unittest import TestCase
from unittest.mock import patch
from lab05 import print_character
import io


class TestPrint_character(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character(self):
        character = ["Bahedi", ["Strength", ]]
        print_character()

