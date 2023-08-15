import unittest

from tire.Octoprime import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tirewear = [0.9, 0.7, 0.7, 0.9]
        tire = OctoprimeTire(tirewear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tirewear = [0.1, 0.2, 0.4, 0.6]
        tire = OctoprimeTire(tirewear)
        self.assertFalse(tire.needs_service())
