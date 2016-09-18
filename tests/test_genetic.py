import unittest

from main import crossover


class TestGenetic(unittest.TestCase):
    def setUp(self):
        self.test_parent_a = ['00000110.101010110011010001111110', '10001000.101101001101111011101000',
                              '00001001.000100001001111010000110', '00001000.001111110010111111111100']
        self.test_parent_b = ['00001001.001010000001100110010111', '10000000.110010000101010011110110',
                              '10000100.001110110010000001100000', '10000011.011011010100101010111111']
        self.test_separator = 2
        self.test_child = ['00000110.101010110011010001111110', '10001000.101101001101111011101000',
                           '10000100.001110110010000001100000', '10000011.011011010100101010111111']

    def test_crossover_func(self):
        parent_a = self.test_parent_a
        parent_b = self.test_parent_b
        separator = self.test_separator
        child = self.test_child
        self.assertEquals(child, crossover(parent_a, parent_b, separator))

    def tearDown(self):
        pass
