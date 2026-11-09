
import unittest

from operations import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    exponentiation,
    floor_division
)


class TestCalculatorOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)

    def test_subtract(self):
        self.assertEqual(subtract(20, 10), 10)

    def test_multiply(self):
        self.assertEqual(multiply(5, 4), 20)

    def test_divide(self):
        self.assertEqual(divide(20, 5), 4)

    def test_divide_decimal(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)

    def test_exponentiation(self):
        self.assertEqual(exponentiation(2, 3), 8)

    def test_floor_division(self):
        self.assertEqual(floor_division(10, 3), 3)


if __name__ == "__main__":
    unittest.main()
