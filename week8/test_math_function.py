import os
import sys
import unittest

from week8.math_function import modulo_func, is_even, is_odd, sum_function, sub_function, mul_function, \
    div_function

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '')))


class TestMathFunction(unittest.TestCase):
    def test_modulo_func(self):
        self.assertEqual(modulo_func(10), 0)
        self.assertEqual(modulo_func(11), 1)
        self.assertEqual(modulo_func(0), 0)
        self.assertEqual(modulo_func(-1), -1)

    def test_is_even(self):
        self.assertTrue(is_even(6))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(-1))

    def test_is_odd(self):
        self.assertTrue(is_odd(7))
        self.assertTrue(is_odd(-1))
        self.assertFalse(is_odd(6))
        self.assertFalse(is_odd(0))

    def test_sum_function(self):
        self.assertEqual(sum_function(5, 6), 11)
        self.assertEqual(sum_function(-1, 1), 0)
        self.assertEqual(sum_function(-5, -6), -11)
        self.assertEqual(sum_function(0, 0), 0)

    def test_sub_function(self):
        self.assertEqual(sub_function(11, 6), 5)
        self.assertEqual(sub_function(0, 6), -6)
        self.assertEqual(sub_function(-11, -6), -5)
        self.assertEqual(sub_function(6, 0), 6)

    def test_mul_function(self):
        self.assertEqual(mul_function(3, 4), 12)
        self.assertEqual(mul_function(0, 4), 0)
        self.assertEqual(mul_function(-3, 4), -12)
        self.assertEqual(mul_function(-3, -4), 12)

    def test_div_function(self):
        self.assertEqual(div_function(12, 4), 3)
        self.assertEqual(div_function(-12, 4), -3)
        self.assertEqual(div_function(-12, -4), 3)
        with self.assertRaises(ValueError):
            div_function(12, 0)
