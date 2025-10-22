import unittest
from feasibility_app import analyze_feasibility


class FeasibilityTest(unittest.TestCase):
    def test_positive_roi(self):
        result = analyze_feasibility(100, 150, discount_rate=0.1, years=1)
        self.assertTrue(result["feasible"])
        expected_roi = (150 / 1.1 - 100) / 100
        self.assertAlmostEqual(result["roi"], expected_roi, places=6)

    def test_negative_roi(self):
        result = analyze_feasibility(200, 150, discount_rate=0.1, years=1)
        self.assertFalse(result["feasible"])
        expected_roi = (150 / 1.1 - 200) / 200
        self.assertAlmostEqual(result["roi"], expected_roi, places=6)


if __name__ == "__main__":
    unittest.main()
