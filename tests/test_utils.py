import unittest

from utils import coder


class TestCoder(unittest.TestCase):
    def setUp(self):
        self.test_real_num_in_str = "246"
        self.test_real_num_bin = "001111101111100111011011001"

        self.test_integer_num = 34
        self.test_integer_num_bin = "0100010"

    def test_real_part_to_bin(self):
        real_num = self.test_real_num_in_str
        real_num_bin = coder.real_part_to_bin(real_num)
        self.assertEquals(real_num_bin, self.test_real_num_bin)

    def test_integer_part_to_bin(self):
        int_num = self.test_integer_num
        int_num_bin = coder.integer_part_to_bin(int_num)
        self.assertEquals(int_num_bin, self.test_integer_num_bin)

    def tearDown(self):
        pass
