import unittest

from utils import coder


class TestCoder(unittest.TestCase):
    def setUp(self):
        self.test_real_num = "246"
        self.test_real_num_bin = "001111101111100111011011001"

    def test_real_part_to_bin(self):
        real_num = self.test_real_num
        real_num_bin = coder.real_part_to_bin(real_num)
        self.assertEquals(real_num_bin, str(self.test_real_num_bin))

    def tearDown(self):
        pass
