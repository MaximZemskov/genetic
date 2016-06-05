import unittest
import sys

from test_utils import TestCoder
from test_chromosome import TestChromosome

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(TestCoder),
        unittest.makeSuite(TestChromosome),

    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
