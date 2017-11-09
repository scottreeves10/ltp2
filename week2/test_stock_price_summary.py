import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary_empty_list(self):
        '''Test stock_price_summary with empty list'''

        actual = a1.stock_price_summary([])
        expected = (0.0, 0.0)

        self.assertEqual(expected, actual)

    def test_stock_price_summary_only_zero(self):
        '''Test stock_price_summary with only zero'''

        actual = a1.stock_price_summary([0.00])
        expected = (0.00, 0.0)

        self.assertEqual(expected, actual)

    def test_stock_price_summary_only_non_negative(self):
        '''Test stock_price_summary with only a non-negative'''

        actual = a1.stock_price_summary([0.05])
        expected = (0.05, 0.0)

        self.assertEqual(expected, actual)

    def test_stock_price_summary_only_negative(self):
        '''Test stock_price_summary with only a negative'''

        actual = a1.stock_price_summary([-0.05])
        expected = (0.00, -0.05)

        self.assertEqual(expected, actual)

    def test_stock_price_summary_including_zero(self):
        '''Test stock_price_summary including at least one zero'''

        actual = a1.stock_price_summary([0, 1, 0, -1, 0])
        expected = (1.0, -1.0)

        self.assertEqual(expected, actual)

    def test_stock_price_summary_multiple_alternating(self):
        '''Test stock_price_summary with multiple alternating gains and losses'''

        actual = a1.stock_price_summary([0.7, -0.6, 1, -1, 2.11, -3.33])
        expected = (3.81, -4.93)

        self.assertEqual(expected, actual)

    def test_stock_price_summary_multiple_adjacent(self):
        '''Test stock_price_summary with multiple adjacent gains and losses'''

        actual = a1.stock_price_summary([-0.25, -0.67, -0.99, -1.23, 0.33, 3.12, 0.99, .02])
        expected = (4.46, -3.14)

        self.assertEqual(expected, actual)

    def test_stock_price_summary_multiple_alternating_values_and_zeroes(self):
        '''Test stock_price_summary with zeroes at the beginning, in middle and at the end of the list'''

        actual = a1.stock_price_summary([0, 0.7, -0.6, 1, 0, -1, 2.11, -3.33, 0])
        expected = (3.81, -4.93)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
