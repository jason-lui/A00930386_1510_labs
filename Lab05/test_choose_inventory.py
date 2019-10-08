from unittest import TestCase
from unittest.mock import patch
from lab05 import choose_inventory
import io


class TestChoose_inventory(TestCase):

    @patch("random.sample", sample_items = ['Rapidfire Cannon', 'Boots of Lucidity'])
    def test_choose_inventory_0_0(self, mock_items):
        inventory = []
        selection = 0
        self.assertEqual([], choose_inventory(inventory, selection))

    @patch("random.sample", sample_items = ['Rapidfire Cannon', 'Boots of Lucidity'])
    def test_choose_inventory_4_0(self, mock_items):
        inventory = ['Rabadon\'s Deathcap', 'Abyssal\' Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        selection = 0
        self.assertEqual([], choose_inventory(inventory, selection))

    @patch("random.sample", sample_items = ['Rapidfire Cannon', 'Boots of Lucidity'])
    def test_choose_inventory_0_4(self, mock_items):
        inventory = []
        selection = 4
        self.assertEqual([], choose_inventory(inventory, selection))

    @patch("random.sample", sample_items = ['Rapidfire Cannon', 'Boots of Lucidity'])
    def test_choose_inventory_4_(self, mock_items):
        inventory = ['Rabadon\'s Deathcap', 'Abyssal\' Mask', 'Rapidfire Cannon', 'Boots of Lucidity']
        selection = 0
        self.assertEqual([], choose_inventory(inventory, selection))