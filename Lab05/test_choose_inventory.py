from unittest import TestCase
from unittest.mock import patch
from lab05 import choose_inventory
import io


class TestChoose_inventory(TestCase):

    @patch("random.sample", side_effect=[[], [], [], []])
    def test_choose_inventory_0_0(self, mock_items):
        inventory = []
        selection = 0
        expected = []
        self.assertEqual(expected, choose_inventory(inventory, selection))

    @patch("random.sample", side_effect=[[], [], [], []])
    def test_choose_inventory_4_0(self, mock_items):
        inventory = ['Rabadon\'s Deathcap', 'Abyssal\' Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        selection = 0
        expected = []
        self.assertEqual(expected, choose_inventory(inventory, selection))

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.sample", side_effect=[[], [], [], []])
    def test_choose_inventory_0_n1(self, mock_items, mock_output):
        inventory = []
        selection = -1
        expected = []
        expected_string = "WARNING: The number of items selected is negative.\n"
        self.assertEqual(expected, choose_inventory(inventory, selection))
        self.assertEqual(expected_string, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.sample", side_effect=[[], [], [], []])
    def test_choose_inventory_4_n1(self, mock_items, mock_output):
        inventory = ['Rabadon\'s Deathcap', 'Abyssal\' Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        selection = -1
        expected = []
        expected_string = "WARNING: The number of items selected is negative.\n"
        self.assertEqual(expected, choose_inventory(inventory, selection))
        self.assertEqual(expected_string, mock_output.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("random.sample", side_effect=[[], [], [], []])
    def test_choose_inventory_0_4(self, mock_items, mock_output):
        inventory = []
        selection = 4
        expected = []
        expected_string = "WARNING: The number of items selected is larger than the size of the inventory.\n"
        self.assertEqual(expected, choose_inventory(inventory, selection))
        self.assertEqual(expected_string, mock_output.getvalue())

    @patch("random.sample", side_effect=[['Rapidfire Cannon', 'Boots of Lucidity']])
    def test_choose_inventory_4_2(self, mock_items):
        inventory = ['Rabadon\'s Deathcap', 'Abyssal\' Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        selection = 2
        self.assertEqual(['Boots of Lucidity', 'Rapidfire Cannon'], choose_inventory(inventory, selection))