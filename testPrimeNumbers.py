""" Tests our prime number function """

import unittest
from primeNumbers import primeNumbers

class TestPrimeNumbers(unittest.TestCase):
    """ Tests prime_numbers functionality """

    def test_input_is_not_positive(self):
        self.assertEqual(primeNumbers(-5), [])
    def test_input_is_not_int(self):
    	self.assertRaises(TypeError,primeNumbers, [2,4])
    def test_valid_primeNumbers(self):
        self.assertEqual(primeNumbers(8), [2,3,5,7])
if __name__ == "__main__":
    unittest.main(exit = False)
