# coding=utf-8

# noinspection PyUnresolvedReferences
from strictint import StrictInt  # This works, but PyCharm complains about this, so suppress warnings.
from fractions import Fraction
from decimal import Decimal
import unittest


class TestStrictInt(unittest.TestCase):

    def test_float_conversion(self):
        # Non-integer parts present in a float, should raise ValueError
        self.assertRaises(ValueError, StrictInt, 3.14159)
        # Float that is equal to an int should be equal.
        self.assertEqual(3.0, StrictInt(3.0))

    def test_ints(self):
        # int(3) should equal StrictInt(3).
        self.assertEqual(3, StrictInt(3))

    def test_nonnumeric_string(self):
        # Not a number at all.
        self.assertRaises(ValueError, StrictInt, "I Am A Teapot")
        # Number with an invalid character in it, so Not a Number.
        self.assertRaises(ValueError, StrictInt, " 3.14159")
        # Has numeric content, but not a valid number due to dots.
        self.assertRaises(ValueError, StrictInt, "3.14.156")

    def test_numeric_string(self):
        # int('3') should equal StrictInt('3')
        self.assertEqual(int('3'), StrictInt('3'))
        # int(float('3.0')) is equal to int(3.0), and should equal StrictInt('3.0')
        self.assertEqual(int(float('3.0')), StrictInt('3.0'))
        # String with a number that has a decimal part should raise ValueError
        self.assertRaises(ValueError, StrictInt, '3.14159')

    def test_complex(self):
        # Test Fraction type complex arguments.
        self.assertEqual(int(Fraction(10, 2)), StrictInt(Fraction(10, 2)))  # Fraction(10, 2) == 5
        self.assertRaises(ValueError, StrictInt, Fraction(10, 3))  # TypeError: Fractional part.

        # Test Decimal type complex arguments.
        self.assertEqual(Decimal('11.00000'), StrictInt(Decimal('11.00000')))  # String rep of 11
        self.assertRaises(ValueError, StrictInt, Decimal('11.00001'))  # TypeError: Fractional part.

        # Test complex equation(s)
        self.assertEqual(5, StrictInt(5+0j))  # 5+0j reduces to 5, so it should equal 5.
        self.assertRaises(ValueError, StrictInt, 5+1j)  # Non-zero imaginary part.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
