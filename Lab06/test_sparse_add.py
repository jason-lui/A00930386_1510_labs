from unittest import TestCase
from sparsevector import sparse_add


class TestSparse_add(TestCase):

    def test_sparse_add_both_empty(self):
        v1 = {}
        v2 = {}
        expected = {}
        self.assertEqual(expected, sparse_add(v1, v2))

    def test_sparse_add_v1_empty(self):
        v1 = {}
        v2 = {0: 1, 1: 2, 2: 3, 3: 4}
        expected = {0: 1, 1: 2, 2: 3, 3: 4}
        self.assertEqual(expected, sparse_add(v1, v2))

    def test_sparse_add_v2_empty(self):
        v1 = {0: 1, 1: 2, 2: 3, 3: 4}
        v2 = {}
        expected = {0: 1, 1: 2, 2: 3, 3: 4}
        self.assertEqual(expected, sparse_add(v1, v2))

    def test_sparse_add(self):
        v1 = {0: 1, 1: 2, 2: 3, 3: 4}
        v2 = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6}
        expected = {0: 1, 1: 2, 2: 4, 3: 6, 4: 3, 5: 4, 6: 5, 7: 6}
        self.assertEqual(expected, sparse_add(v1, v2))
