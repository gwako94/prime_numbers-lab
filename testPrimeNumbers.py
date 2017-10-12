""" Tests our prime number function """

import unittest
from primeNumbers import primeNumbers

class TestPrimeNumbers(unittest.TestCase):
    """ Tests prime_numbers functionality """

    def test_input_is_positive(self):
        self.assertEqual(primeNumbers(-5), [])
    def test_input_is_Not_a_list(self):
    	self.assertRaises(TypeError,primeNumbers, [2,4])
    def test_input_is_zero(self):
        self.assertEqual(primeNumbers(0), [])
    def test_output_is_primeNumbers(self):
        self.assertEqual(primeNumbers(8), [2,3,5,7])
    def test_input_is_not_a_dictionary(self):
        self.assertRaises(TypeError,primeNumbers, {"jane":2, "tom":4})
if __name__ == "__main__":
    unittest.main(exit = False)
