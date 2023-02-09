import unittest

from exercice1 import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        result = self.calc.subtract(2, 1)
        self.assertEqual(result, 1)

    def test_multiply(self):
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = self.calc.divide(6, 3)
        self.assertEqual(result, 2)

    def test_power(self):
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)

    def test_square_root(self):
        result = self.calc.square_root(1)
        self.assertEqual(result, 1)

# Afficher le checking des test
if __name__ == '__main__':
    unittest.main()