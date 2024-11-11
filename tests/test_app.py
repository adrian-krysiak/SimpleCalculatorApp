import unittest
from app import add, delete, multiply, divide, load_results, mean

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2, 3), 6)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0, 0), 0)

    def test_delete(self):
        self.assertEqual(delete(10, 5), 5)
        self.assertEqual(delete(0, 5), -5)
        self.assertEqual(delete(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(-3, 4), -12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), "Error: Division by zero")
        self.assertEqual(divide(9, 3), 3)

    def test_operations_mixed(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(delete(5, 3), 2)
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(divide(10, 2), 5)

    def test_divide_zero(self):
        self.assertEqual(divide(10, 0), "Error: Division by zero")

    def test_add_empty(self):
        self.assertEqual(add(), 0)

    def test_negative_operations(self):
        self.assertEqual(delete(-5, -3), -2)
        self.assertEqual(multiply(-3, -2), 6)

    def test_load_results(self):
        self.assertIsInstance(load_results(), list)

    def test_invalid_argument_delete(self):
        """Test that 'delete' raises an error with less than 2 numbers"""
        with self.assertRaises(TypeError) as context:
            delete(5)
        # Check if the error message contains the expected message
        self.assertIn("missing 1 required positional argument", str(context.exception))

    def test_mean_operation(self):
        """Test that 'mean' calculates the average correctly"""
        self.assertEqual(mean((2, 8)), 5)
        

if __name__ == "__main__":
    unittest.main()
