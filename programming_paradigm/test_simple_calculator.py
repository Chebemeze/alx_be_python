import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
  def setUp(self):
    self.calc = SimpleCalculator()
  
  def test_addition(self):
    """Test the addition method."""
    self.assertEqual(self.calc.add(2, 3), 5)
    self.assertEqual(self.calc.add(-1, 1), 0)
    self.assertEqual(self.calc.add(-1, -1), -2)
    self.assertEqual(self.calc.add(0, -1), -1)
    self.assertAlmostEqual(self.calc.add(0.5, 5.0), 5.5)
    self.assertAlmostEqual(self.calc.add(-0.5, -5.0), -5.5)
    self.assertAlmostEqual(self.calc.add(-0.5, 5.0), 4.5)
    self.assertAlmostEqual(self.calc.add(0.5, -5.0), -4.5)
    # Add more assertions to thoroughly test the add method.

  def test_subtraction(self):
    self.assertEqual(self.calc.subtract(-1, -1), 0)
    self.assertEqual(self.calc.subtract(5, 2), 3)
    self.assertEqual(self.calc.subtract(5, -1), 6)
    self.assertEqual(self.calc.subtract(-1, 5), -6)
    self.assertEqual(self.calc.subtract(0, 0), 0)
    self.assertAlmostEqual(self.calc.subtract(0.5, 5.0), -4.5)
    self.assertAlmostEqual(self.calc.subtract(-0.5, -5.0), 4.5)
    self.assertAlmostEqual(self.calc.subtract(0.5, -5.0), 5.5)
    self.assertAlmostEqual(self.calc.subtract(-0.5, 5.0), -5.5)
  
  def test_multiply(self):
    self.assertEqual(self.calc.multiply(-1, -1), 1)
    self.assertEqual(self.calc.multiply(4, 10), 40)
    self.assertEqual(self.calc.multiply(100, 100), 10000)
    self.assertEqual(self.calc.multiply(-5, 8), -40)
    self.assertEqual(self.calc.multiply(5, -8), -40)
    self.assertAlmostEqual(self.calc.multiply(-0.5, -5.0), 2.5)
    self.assertAlmostEqual(self.calc.multiply(-0.5, 5.0), -2.5)
    self.assertAlmostEqual(self.calc.multiply(0.5, -5.0), -2.5)
    self.assertAlmostEqual(self.calc.multiply(0.5, 5.0), 2.5)
  
  def test_divide(self):
    self.assertEqual(self.calc.divide(-1, -1), 1)
    self.assertEqual(self.calc.divide(5, 2), 2.5)
    self.assertEqual(self.calc.divide(7, -3), -2.3333333333333335)
    self.assertEqual(self.calc.divide(-20, 2), -10)
    self.assertAlmostEqual(self.calc.divide(10.0, 0.5), 20)
    self.assertAlmostEqual(self.calc.divide(-20.5, 0.5), -41.0)

    """The above code addresses ZeroDivisionError. the test is successful when None is returned"""
    self.assertIsNone(self.calc.divide(0, 0))
    self.assertIsNone(self.calc.divide(60, 0))

# Remember to write additional test methods for subtract, multiply, and divide.


# if __name__ == "__main__":
#   unittest.main()