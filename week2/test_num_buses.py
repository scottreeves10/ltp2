import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses_at_zero(self):
        '''Test num_buses at boundary of Precondition: n >= 0'''

        actual = a1.num_buses(0)
        expected = 0

        self.assertEqual(expected, actual)
        

    def test_num_buses_next_for_one_person(self):
        '''Test num_buses next to boundary of Precondition: n >= 0'''

        actual = a1.num_buses(1)
        expected = 1

        self.assertEqual(expected, actual)
        

    def test_num_buses_in_range_for_one_bus(self):
        '''Test num_buses where number of people referes to a value >= 1 and <= 49'''

        actual = a1.num_buses(49)
        expected = 1

        self.assertEqual(expected, actual)
        


    def test_num_buses_equal_to_single_bus_threshhold(self):
        '''Test num_buses where number of people refers to the value which is Equal to the threshold requiring a Single bus'''

        actual = a1.num_buses(50)
        expected = 1

        self.assertEqual(expected, actual)
        

    def test_num_buses_following_single_bus_threshhold(self):
        '''Test num_buses where number of people refers to the value which Follows the threshold requiring a Single bus'''

        actual = a1.num_buses(51)
        expected = 2

        self.assertEqual(expected, actual)
        

    def test_num_buses_middle_range_for_multiple_buses(self):
        '''Test num_buses where number of people refers to a value which falls near the middle of the range requiring Multiple buses'''

        actual = a1.num_buses(80)
        expected = 2

        self.assertEqual(expected, actual)


    def test_num_buses_at_even_multiple_of_50(self):
        '''TTest num_buses where number of people refers to the value which is Equal to the threshold requiring and Even number Multiple buses'''

        actual = a1.num_buses(100)
        expected = 2

        self.assertEqual(expected, actual)


    def test_num_buses_at_odd_multiple_of_buses(self):
        '''Test num_buses where the number of people refers to a value Equal to a threshold which requires an Odd number Multiple buses'''

        actual = a1.num_buses(150)
        expected = 3

        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main(exit=False)
