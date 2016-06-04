import unittest

from utils import coder


class TestCoder(unittest.TestCase):
    def setUp(self):
        #######
        # test_real_part_to_bin_func
        #######
        self.test_real_num_in_str = "246"
        self.test_real_num_bin = "001111101111100111011011"

        #######
        # test_integer_part_to_bin_func
        #######
        self.test_integer_num = 34
        self.test_integer_num_bin = "0100010"

        #######
        # test_code_func_with_positive_num
        #######
        self.test_positive_num = 1.426
        self.test_positive_num_in_bin = "00000001.011011010000111001010110"

        #######
        # test_code_func_with_negative_num
        #######
        self.test_negative_num = -1.11155
        self.test_negative_num_in_bin = "10000001.000111001000111010001010"

    def test_real_part_to_bin_func(self):
        real_num = self.test_real_num_in_str
        real_num_bin = coder.real_part_to_bin(real_num)
        self.assertEquals(real_num_bin, self.test_real_num_bin)

    def test_integer_part_to_bin_func(self):
        int_num = self.test_integer_num
        int_num_bin = coder.integer_part_to_bin(int_num)
        self.assertEquals(int_num_bin, self.test_integer_num_bin)

    def test_code_func_with_positive_num(self):
        num = self.test_positive_num
        num_bin = coder.code(num)
        self.assertEquals(num_bin, self.test_positive_num_in_bin)

    def test_code_func_with_negative_num(self):
        num = self.test_negative_num
        num_bin = coder.code(num)
        self.assertEquals(num_bin, self.test_negative_num_in_bin)

    def tearDown(self):
        pass
