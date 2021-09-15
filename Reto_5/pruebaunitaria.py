import unittest
import Geometria as g
from View import View as v

geo = g.Geometria(2, 2, 3)
view = v()
select = view.select(geo)

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
        if geo.figuraName == "Cuadrado":
            self.assertIs(geo.switch(1), 4)
            print('tearDown() -> OK')
            # result = geo.areaCuadrado(geo.a)
            # self.assertEqual(result, 4)
            # print('tearDown() -> OK')

    def test_areacirculo(self):
        """
        Tests that it can calculate the area of a circle
        """
        if geo.figuraName == "Circulo":
            self.assertIs(geo.switch(2), 12.5664)
        # result = geo.areaCirculo(2)
        # self.assertEqual(result, 12.5664)
        # print('tearDown() -> OK')

    def test_areatriangulo(self):
        """
        Tests that it can calculate the area of a triangle
        """
        if geo.figuraName == "Triangulo":
            self.assertIs(geo.switch(3), 2)
        # result = geo.areaTriangulo(2, 3)
        # self.assertEqual(result, 3)
        # print('tearDown() -> OK')

    def test_arearectangulo(self):
        """
        Tests that it can calculate the area of a rectangle
        """
        if geo.figuraName == "Rectangulo":
            self.assertIs(geo.switch(4), 4)
        # result = geo.areaRectangulo(4, 2)
        # self.assertEqual(result, 8)
        # print('tearDown() -> OK')

    def test_areapentagono(self):
        """
        Tests that it can calculate the area of a pentagon
        """
        if geo.figuraName == "Pentagono":
            self.assertIs(geo.switch(5), 2)
        # result = geo.areaPentagono(3, 2)
        # self.assertEqual(result, 3)
        # print('tearDown() -> OK')

    def test_arearombo(self):
        """
        Tests that it can calculate the area of a rhombus
        """
        if geo.figuraName == "Rombo":
            self.assertIs(geo.switch(6), 2)
        # result = geo.areaRombo(6, 2)
        # self.assertEqual(result, 6)
        # print('tearDown() -> OK')

    def test_arearomboide(self):
        """
        Tests that it can calculate the area of a rhomboid
        """
        if geo.figuraName == "Romboide":
            self.assertIs(geo.switch(7), 4)
        # result = geo.areaRomboide(3, 3)
        # self.assertEqual(result, 9)
        # print('tearDown() -> OK')

    def test_areatrapecio(self):
        """
        Tests that it can calculate the area of a trapezoid
        """
        if geo.figuraName == "Trapecio":
            self.assertIs(geo.switch(8), 6)
        # result = geo.areaTrapecio(2, 2, 2)
        # self.assertEqual(result, 4)
        # print('tearDown() -> OK')

    def tearDown(self):
        print('tearDown() -> OK')


if __name__ == '__main__':
    unittest.main()