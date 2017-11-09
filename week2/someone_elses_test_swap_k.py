import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_empty(self):
        """
        Test a1.swap_k when L is an empty list (note that precondition implies
        k == 0)
        """
        L = []
        k = 0
        expected = []
        a1.swap_k(L,k)
        self.assertEqual(expected,L)


    def test_swap_k_odd_length_list(self):
        """
        Test a1.swap_k when L is an odd length list
        """
        L = ['a','c','asdasd',3,'13as']
        k = 2
        expected = [3,'13as','asdasd','a','c']
        a1.swap_k(L,k)
        self.assertEqual(expected,L)


    def test_swap_k_even_length_list(self):
        """
        Test a1.swap_k when L is an even length list
        """
        L = ['a','b','c',1,2,3]
        k = 1
        expected = [3,'b','c',1,2,'a']
        a1.swap_k(L,k)
        self.assertEqual(expected,L)


    def test_swap_k_when_k_equals_half_length(self):
        """
        Test a1.swap_k when k = len(L)/2
        """
        L = ['a','b','c',1,2,3]
        k = 3
        expected = [1,2,3,'a','b','c']
        a1.swap_k(L,k)
        self.assertEqual(expected,L)




    def test_swap_k_when_k_equals_0(self):
        """
        Test a1.swap_k when k equals zero
        """
        L = ['a','b',3,'adf','asdsad']
        k = 0
        expected = ['a','b',3,'adf','asdsad']
        a1.swap_k(L,k)
        self.assertEqual(expected,L)
        
        
        
if __name__ == '__main__':
    unittest.main(exit=False)
