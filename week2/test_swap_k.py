import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """


    def test_swap_k_empty_list(self):
        '''Test swap_k with an empty list'''

        k = 0
        L = []
        a1.swap_k(L, k)
        actual = L
        expected = []

        self.assertEqual(expected, actual)


    def test_swap_k_one_item_list(self):
        '''Test swap_k with a list containing one item, and where k = 0 satisfies the Precondtion: 0 <= k <= len(L) // 2'''

        k = 0
        L = ['abcd']
        a1.swap_k(L, k)
        actual = L
        expected = ['abcd']

        self.assertEqual(expected, actual)


    def test_swap_k_two_item_list(self):
        '''Test swap_k with a list containing two items, and where k = 1 satisfies the Precondtion: 0 <= k <= len(L) // 2'''

        k = 1
        L = ['abcd', 'xyx']
        a1.swap_k(L, k)
        actual = L
        expected = ['xyx', 'abcd']

        self.assertEqual(expected, actual)


    def test_swap_k_list_of_int(self):
        '''Test swap_k with a list of int '''

        k = 2
        L = [1, 2, 3, 4, 5, 6]
        a1.swap_k(L, k)
        actual = L
        expected = [5, 6, 3, 4, 1, 2]

        self.assertEqual(expected, actual)


    def test_swap_k_list_of_str(self):
        '''Test swap_k with a list of str '''

        k = 2
        L = ['a', 'b', 'c', 'd', 'e', 'f']
        a1.swap_k(L, k)
        actual = L
        expected = ['e', 'f', 'c', 'd', 'a', 'b']

        self.assertEqual(expected, actual)


    def test_swap_k_list_of_lists(self):
        '''Test swap_k with a list of lists '''

        k = 3
        L = [['a'], ['b'], ['c'], ['d'], ['e'], ['f']]
        a1.swap_k(L, k)
        actual = L
        expected = [['d'], ['e'], ['f'], ['a'], ['b'], ['c']]

        self.assertEqual(expected, actual)
        

    def test_swap_k_list_of_dicts(self):
        '''Test swap_k with a list of dicts '''

        k = 1
        L = [{'z' : 1, 'y' : 2}, {'abc' : 3}, {'def' : 4}, {'ghi' : 5}]
        a1.swap_k(L, k)
        actual = L
        expected = [{'ghi' : 5}, {'abc' : 3}, {'def' : 4}, {'z' : 1, 'y' : 2}]

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
