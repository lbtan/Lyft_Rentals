import unittest

from tire.Carrigan import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tirewear = [0.1, 0.2, 0.4, 0.9]
        tire = CarriganTire(tirewear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tirewear = [0.1, 0.2, 0.4, 0.5]
        tire = CarriganTire(tirewear)
        self.assertFalse(tire.needs_service())
