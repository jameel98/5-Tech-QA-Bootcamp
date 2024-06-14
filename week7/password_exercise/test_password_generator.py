import string
import unittest

from week7.password_exercise.pass_generator import generate_password


class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        for length in range(1, 101):
            password = generate_password(length)
            self.assertEqual(len(password), length, f"Failed for length: {length}")

    def test_password_contains_characters(self):
        password = generate_password(100)
        self.assertTrue(any(c in string.ascii_uppercase for c in password), "Password does not contain uppercase letters")
        self.assertTrue(any(c in string.ascii_lowercase for c in password), "Password does not contain lowercase letters")
        self.assertTrue(any(c in string.digits for c in password), "Password does not contain digits")
        self.assertTrue(any(c in string.punctuation for c in password), "Password does not contain punctuation")

    def test_zero_length_password(self):
        with self.assertRaises(ValueError):
            generate_password(0)

    def test_negative_length_password(self):
        with self.assertRaises(ValueError):
            generate_password(-1)

    def test_non_integer_length(self):
        with self.assertRaises(ValueError):
            generate_password('a')
        with self.assertRaises(ValueError):
            generate_password(5.5)

if __name__ == "__main__":
    unittest.main()
