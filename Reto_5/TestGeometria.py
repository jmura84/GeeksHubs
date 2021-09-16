'''
Este módulo es una práctica de tests unitarios para poner a prueba las partes de los módulos View y Geometría.
'''

__author__ = 'Javier Muñoz Ramón'
__copyright__ = 'Copyright (c) 2021. All rights are reserved.'
__license__ = 'GPL 3'


import unittest
from unittest.mock import patch
import Geometria as g
import View as v

geo = g.Geometria(2, 2, 3)
view = v.View()


class TestGeometria(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass() -> OK')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass() -> OK')

    def setUp(self):
        print('SetUp() -> OK')


    '''
    Con la línea del decorador @patch, en la parte de side_effect, se añade un input de usuario concreto.
    Al añadir mock_input como argumento del siguiente método, este input se introduce automáticamente cuando
    el método select se lo pida.
    '''
    @patch('builtins.input', side_effect=[1])
    def test_areacuadrado(self, mock_input):
        """
        Prueba que calcule el área de un cuadrado.
        """
        view.select(geo)
        print(geo.figuraName)
        self.assertIs(geo.figuraName, "Cuadrado")
        self.assertEqual(geo.switch(1), 4)
        print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[2])
    def test_areacirculo(self, mock_input):
        """
        Prueba que calcule el área de un círculo.
        """
        view.select(geo)
        print(geo.figuraName)
        self.assertIs(geo.figuraName, "Circulo")
        self.assertEqual(geo.switch(2), 12.5664)
        print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[3])
    def test_areatriangulo(self, mock_input):
        """
        Prueba que calcule el área de un triángulo.
        """
        view.select(geo)
        print(geo.figuraName)
        self.assertIs(geo.figuraName, "Triangulo")
        self.assertEqual(geo.switch(3), 2)
        print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[4])
    def test_arearectangulo(self, mock_input):
        """
        Prueba que calcule el área de un rectángulo.
        """
        view.select(geo)
        print(geo.figuraName)
        self.assertIs(geo.figuraName, "Rectangulo")
        self.assertEqual(geo.switch(4), 4)
        print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[5])
    def test_areapentagono(self, mock_input):
        """
        Prueba que calcule el área de un pentágono.
        """
        view.select(geo)
        print(geo.figuraName)
        self.assertIs(geo.figuraName, "Pentagono")
        self.assertEqual(geo.switch(5), 2.0)
        print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[6])
    def test_arearombo(self, mock_input):
        """
        Prueba que calcule el área de un rombo.
        """
        view.select(geo)
        print(geo.figuraName)
        self.assertIs(geo.figuraName, "Rombo")
        self.assertEqual(geo.switch(6), 2)
        print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[7])
    def test_arearomboide(self, mock_input):
        """
        Prueba que calcule el área de un romboide.
        """
        view.select(geo)
        print(geo.figuraName)
        self.assertIs(geo.figuraName, "Romboide")
        self.assertEqual(geo.switch(7), 4)
        print('tearDown() -> OK')

    @patch('builtins.input', side_effect=[8])
    def test_areatrapecio(self, mock_input):
        """
        Prueba que calcule el área de un trapecio.
        """
        view.select(geo)
        print(geo.figuraName)
        self.assertIs(geo.figuraName, "Trapecio")
        self.assertEqual(geo.switch(8), 6)
        print('tearDown() -> OK')

    def tearDown(self):
        print('tearDown() -> OK')


if __name__ == '__main__':
    unittest.main()