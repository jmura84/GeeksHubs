import unittest
from unittest.mock import patch
import Geometria as g
from View import View as v

geo = g.Geometria(2, 2, 3)
view = v()

# select = view.select(geo)

class TestGeometria(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass() -> OK')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass() -> OK')

    def setUp(self):
        print('SetUp() -> OK')

    indexlist = '1 2 3 4 5 6 7 8'

    @patch('builtins.input', side_effect = [1, indexlist])
    def test_areacuadrado(self, mock_input):
        """
        Tests that it calculate the area of a square
        """
        view.select(geo)
        print(geo.figuraName)
        if geo.figuraName == "Cuadrado":
            self.assertEqual(geo.switch(1), 4)
            print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[2, indexlist])
    def test_areacirculo(self, mock_input):
        """
        Tests that it can calculate the area of a circle
        """
        view.select(geo)
        print(geo.figuraName)
        if geo.figuraName == "Circulo":
            self.assertEqual(geo.switch(2), 12.5664)
            print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[3, indexlist])
    def test_areatriangulo(self, mock_input):
        """
        Tests that it can calculate the area of a triangle
        """
        view.select(geo)
        print(geo.figuraName)
        if geo.figuraName == "Triangulo":
            self.assertEqual(geo.switch(3), 2)
            print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[4, indexlist])
    def test_arearectangulo(self, mock_input):
        """
        Tests that it can calculate the area of a rectangle
        """
        view.select(geo)
        print(geo.figuraName)
        if geo.figuraName == "Rectangulo":
            self.assertEqual(geo.switch(4), 4)
            print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[5, indexlist])
    def test_areapentagono(self, mock_input):
        """
        Tests that it can calculate the area of a pentagon
        """
        view.select(geo)
        print(geo.figuraName)
        if geo.figuraName == "Pentagono":
            self.assertEqual(geo.switch(5), 2.0)
            print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[6, indexlist])
    def test_arearombo(self, mock_input):
        """
        Tests that it can calculate the area of a rhombus
        """
        view.select(geo)
        print(geo.figuraName)
        if geo.figuraName == "Rombo":
            self.assertEqual(geo.switch(6), 2)
            print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[7, indexlist])
    def test_arearomboide(self, mock_input):
        """
        Tests that it can calculate the area of a rhomboid
        """
        view.select(geo)
        print(geo.figuraName)
        if geo.figuraName == "Romboide":
            self.assertEqual(geo.switch(7), 4)
            print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[8, indexlist])
    def test_areatrapecio(self, mock_input):
        """
        Tests that it can calculate the area of a trapezoid
        """
        view.select(geo)
        print(geo.figuraName)
        if geo.figuraName == "Trapecio":
            self.assertEqual(geo.switch(8), 6)
            print('tearDown() -> OK')

    def tearDown(self):
        print('tearDown() -> OK')


if __name__ == '__main__':
    unittest.main()