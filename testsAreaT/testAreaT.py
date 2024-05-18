import unittest
from src.triangulo import area_triangulo

class TestAreaTriangulo(unittest.TestCase):

    def test_area_triangulo(self):
        self.assertAlmostEqual(area_triangulo(3, 4, 5), 6.0)
        self.assertAlmostEqual(area_triangulo(7, 10, 5), 16.24807680927192)
        self.assertAlmostEqual(area_triangulo(6, 8, 10), 24.0)

    def test_lados_negativos(self):
        with self.assertRaises(ValueError):
            area_triangulo(-3, 4, 5)
        with self.assertRaises(ValueError):
            area_triangulo(3, -4, 5)
        with self.assertRaises(ValueError):
            area_triangulo(3, 4, -5)

    def test_lados_no_validos(self):
        with self.assertRaises(ValueError):
            area_triangulo(1, 2, 3)
        with self.assertRaises(ValueError):
            area_triangulo(1, 10, 12)
        with self.assertRaises(ValueError):
            area_triangulo(5, 5, 10)

if __name__ == "__main__":
    unittest.main()
