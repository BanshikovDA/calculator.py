# test_calculator.py
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    """
    Тестируем функции калькулятора.
    """

    def test_add(self):
        """Тест сложения чисел."""
        result = add(1, 2)
        expected_result = 3
        self.assertEqual(result, expected_result, f"Expected {expected_result}, got {result}")

    def test_subtract(self):
        """Тест вычитания чисел."""
        result = subtract(5, 3)
        expected_result = 2
        self.assertEqual(result, expected_result, f"Expected {expected_result}, got {result}")

if __name__ == "__main__":
    unittest.main()

    def test_multiply(self):
           result = multiply(3, 4)
           expected_result = 12
           self.assertEqual(result, expected_result, f"Expected {expected_result}, got {result}")

    def test_divide(self):
           result = divide(10, 2)
           expected_result = 5
           self.assertEqual(result, expected_result, f"Expected {expected_result}, got {result}")

    def test_divide_by_zero(self):
           with self.assertRaises(ValueError):
               divide(10, 0)