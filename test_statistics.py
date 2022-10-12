from math import sqrt
from statistics import variance, stdev
from unittest import TestCase


class StatisticsTest(TestCase):

    def setUp(self) -> None:
        self.DATASET1 = [10.0, 10.0, 10.0, 10.0, 10.0]
        self.DATASET2 = [1, 2, 3, 4, 5]
        self.DATASET3 = [10, 2, 8, 4, 6]

    def test_variance_typical_values(self):
        """variance of typical values"""
        self.assertEqual(0.0, variance(self.DATASET1))
        self.assertEqual(2.0, variance(self.DATASET2))
        self.assertEqual(8.0, variance(self.DATASET3))

    def test_variance_throws_exception(self):
        """variance of an empty list should raise an exception"""
        with self.assertRaises(ValueError):
            var = variance([])

    def test_standard_deviation(self):
        """standard deviation of typical values"""
        self.assertEqual(0.0, stdev(self.DATASET1))
        self.assertEqual(sqrt(2.0), stdev(self.DATASET2))
        self.assertEqual(sqrt(8.0), stdev(self.DATASET3))


if __name__ == '__main__':
    import unittest
    unittest.main(verbosity=1)
