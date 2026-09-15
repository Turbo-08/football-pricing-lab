import unittest

from pricing import(
    implied_probability,
    calculate_overround,
    fair_odds,
    expected_value
)

class TestPricing(unittest.TestCase):

    def test_implied_probability(self):
        self.assertAlmostEqual(implied_probability(2.00), 0.50)

    def test_overround(self):
        self.assertAlmostEqual(calculate_overround(1.05), 0.05)

    def test_fairodds(self):
        self.assertAlmostEqual(fair_odds(0.40), 2.50)

    def test_expected_value(self):
        self.assertAlmostEqual(expected_value(2.00, 0.60), 0.20)


if __name__ == "__main__":
    unittest.main()

