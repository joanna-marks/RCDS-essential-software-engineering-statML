import unittest
from linear_interpolation import linear_interpolation

class TestLinearInterpolation(unittest.TestCase):
    def test_interpolation_within_range(self):
        self.assertAlmostEqual(linear_interpolation(0, 0, 10, 10, 5), 5)
        self.assertAlmostEqual(linear_interpolation(1, 2, 3, 4, 2), 3)
        self.assertAlmostEqual(linear_interpolation(-1, -1, 1, 1, 0), 0)

    def test_interpolation_outside_range(self):
        with self.assertRaises(ValueError):
            linear_interpolation(0, 0, 10, 10, 11)
        with self.assertRaises(ValueError):
            linear_interpolation(0, 0, 10, 10, -1)

    def test_same_x_values(self):
        with self.assertRaises(ValueError):
            linear_interpolation(1, 1, 1, 2, 1)

    def test_negative_coordinates(self):
        self.assertAlmostEqual(linear_interpolation(-10, -10, 0, 0, -5), -5)
        self.assertAlmostEqual(linear_interpolation(-5, -5, 5, 5, 0), 0)

if __name__ == '__main__':
    unittest.main()