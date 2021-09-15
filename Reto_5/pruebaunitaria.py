import unittest
import Geometria as g

geo = g.Geometria(1, 2, 3)

class TestGeometria(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass() -> OK')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass() -> OK')

    def setUp(self):
        print('SetUp() -> OK')

    def test_areacuadrado(self):
        """
        Tests that it calculate the area of a square
        """
        result = geo.areaCuadrado(2)
        self.assertEqual(result, 4)
        print('tearDown() -> OK')

    def test_areacirculo(self):
        """
        Tests that it can calculate the area of a circle
        """
        result = geo.areaCirculo(2)
        self.assertEqual(result, 12.5664)
        print('tearDown() -> OK')

    def test_areatriangulo(self):
        """
        Tests that it can calculate the area of a triangle
        """
        result = geo.areaTriangulo(2, 3)
        self.assertEqual(result, 3)
        print('tearDown() -> OK')

    def test_arearectangulo(self):
        """
        Tests that it can calculate the area of a rectangle
        """
        result = geo.areaRectangulo(4, 2)
        self.assertEqual(result, 8)
        print('tearDown() -> OK')

    def test_areapentagono(self):
        """
        Tests that it can calculate the area of a pentagon
        """
        result = geo.areaPentagono(3, 2)
        self.assertEqual(result, 3)
        print('tearDown() -> OK')

    def test_arearombo(self):
        """
        Tests that it can calculate the area of a rhombus
        """
        result = geo.areaRombo(6, 2)
        self.assertEqual(result, 6)
        print('tearDown() -> OK')

    def test_arearomboide(self):
        """
        Tests that it can calculate the area of a rhomboid
        """
        result = geo.areaRomboide(3, 3)
        self.assertEqual(result, 9)
        print('tearDown() -> OK')

    def test_areatrapecio(self):
        """
        Tests that it can calculate the area of a trapezoid
        """
        result = geo.areaTrapecio(2, 2, 2)
        self.assertEqual(result, 4)
        print('tearDown() -> OK')

    # def test_set_figuraname(self):
    #     self.assertIs(geo.set_figuraName(geo.a), "Cuadrado")
    #     self.assertIs(geo.set_figuraName(geo.a), "Circulo")
    #     self.assertIs(geo.set_figuraName(geo.a), "Triangulo")

    def tearDown(self):
        print('tearDown() -> OK')


if __name__ == '__main__':
    unittest.main()