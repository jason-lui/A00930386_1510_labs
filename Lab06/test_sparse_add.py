from unittest import TestCase
from sparsevector import sparse_add


class TestSparse_add(TestCase):

    def test_sparse_add_both_empty(self):
        v1 = {}
        v2 = {}
        expected = {}
        self.assertEqual(expected, sparse_add(v1, v2))

    def test_sparse_add_same_indices(self):
        v1 = {1: 1, 2: 2, 99: 3}
        v2 = {1: 2, 2: 4, 99: 6}
        expected = {1: 3, 2: 6, 99: 9}
        self.assertEqual(expected, sparse_add(v1, v2))

    def test_sparse_add_v1_empty(self):
        v1 = {}
        v2 = {0: 1, 1: 2, 2: 3, 99: 4}
        expected = {0: 1, 1: 2, 2: 3, 99: 4}
        self.assertEqual(expected, sparse_add(v1, v2))

    def test_sparse_add_v2_empty(self):
        v1 = {0: 1, 1: 2, 2: 3, 99: 4}
        v2 = {}
        expected = {0: 1, 1: 2, 2: 3, 99: 4}
        self.assertEqual(expected, sparse_add(v1, v2))

    def test_sparse_no_matching_indices(self):
        v1 = {1: 1, 2: 2, 99: 3}
        v2 = {4: 4, 5: 5, 98: 6}
        expected = {1: 1, 2: 2, 4: 4, 5: 5, 98: 6, 99: 3}
        self.assertEqual(expected, sparse_add(v1, v2))

    def test_sparse_some_matching_indices(self):
        v1 = {1: 1, 2: 2, 99: 3}
        v2 = {2: 2, 3: 3, 99: 4}
        expected = {1: 1, 2: 4, 3: 3, 99: 7}
        self.assertEqual(expected, sparse_add(v1, v2))

    def test_sparse_add_to_zero(self):
        v1 = {1: -5, 3: -3, 99: -1}
        v2 = {1: 5, 3: 3, 99: 1}
        expected = {1: 0, 3: 0, 99: 0}
        self.assertEqual(expected, sparse_add(v1, v2))
