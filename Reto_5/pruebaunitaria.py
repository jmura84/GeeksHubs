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

    def test_suma(self):
        """
        Test that it can sum a list of integers
        """
        result = c.sumar(8, 78)
        self.assertEqual(result, 86)
        print('tearDown() -> OK')

    def test_areacuadrado(self):
        result = geo.areaCuadrado(2)
        self.assertEqual(result, 4)
        print('tearDown() -> OK')

    def test_areacirculo(self):
        result = geo.areaCirculo(2)
        self.assertEqual(result, 12.57)
        print('tearDown() -> OK')

    def test_areatriangulo(self):
        result = geo.areaTriangulo(2, 3)
        self.assertEqual(result, 3)
        print('tearDown() -> OK')

    def test_arearectangulo(self):
        result = geo.areaRectangulo(4, 2)
        self.assertEqual(result, 8)
        print('tearDown() -> OK')

    def test_areapentagono(self):
        result = geo.areaPentagono(3, 2)
        self.assertEqual(result, 3)
        print('tearDown() -> OK')

    def test_arearombo(self):
        result = geo.areaRombo(6, 2)
        self.assertEqual(result, 6)
        print('tearDown() -> OK')

    def test_arearomboide(self):
        result = geo.areaRomboide(3, 3)
        self.assertEqual(result, 9)
        print('tearDown() -> OK')

    def test_areatrapecio(self):
        result = geo.areaTrapecio(2, 2, 2)
        self.assertEqual(result, 2)
        print('tearDown() -> OK')

    def tearDown(self):
        print('tearDown() -> OK')


if __name__ == '__main__':
    unittest.main()