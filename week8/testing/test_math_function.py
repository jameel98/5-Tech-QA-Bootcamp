import unittest

from week8.testing.math_function import is_even, is_odd, sum_function, sub_function


class TestMathFunction(unittest.TestCase):
    def test_is_even(self):
        number = 6
        self.assertTrue(is_even(number))

    def test_is_odd(self):
        number = 7
        self.assertTrue(is_odd(number))

    def test_sum_function(self):
        num_a = 5
        num_b = 6
        result = 11

        self.assertEqual(sum_function(num_a, num_b), result)

    def test_sub_function(self):
        num_a = 11
        num_b = 6
        result = 5

        self.assertEqual(sub_function(num_a, num_b), result)

    def test_mul_function(self):
        num_a = 3
        num_b = 4
        result = 12

        self.assertEqual(sub_function(num_a, num_b), result)

    def test_div_function(self):
        num_a = 12
        num_b = 4
        result = 3

        self.assertEqual(sub_function(num_a, num_b), result)






