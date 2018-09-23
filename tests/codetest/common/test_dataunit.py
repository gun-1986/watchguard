import unittest
from common import dataunit


class TestToDataFunction(unittest.TestCase):
    """
    Unit test case for class dataunit.to_data
    """

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_to_data_contains_blank(self):
        self.assertEqual(dataunit.to_data(['3 Gbps', '40 Mbps'],
                                          {'Gbps': 10**9, 'Mbps': 10**6, 'Kbps': 10**3, 'bps': 10**0}),
                         [3*(10**9), 40*(10**6)])

    def test_to_data_no_blank(self):
        self.assertEqual(dataunit.to_data(['3 Gbps', '40 Mbps'],
                                          {'Gbps': 10 ** 9, 'Mbps': 10 ** 6, 'Kbps': 10 ** 3, 'bps': 10 ** 0}),
                         [3 * (10 ** 9), 40 * (10 ** 6)])


if __name__ == '__main__':

    unittest.main()

