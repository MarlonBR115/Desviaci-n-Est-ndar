import math
import unittest

from src.Estadistica import Estadistica,ExceptionDatos


class PruebaEstadistica(unittest.TestCase):
    def setUp(self):
        self.estadistica = Estadistica([])

    def tearDown(self):
        self.estadistica = None

    def test_media_vacio_retornaExcepcion(self):
        self.estadistica.numeros=[]
        with self.assertRaises(ExceptionDatos):
            self.estadistica.calcular_media()

    def test_media_noNumero_retornaExcepcion(self):
        self.estadistica.numeros=[4, 5, "a", 10]
        with self.assertRaises(ExceptionDatos):
            self.estadistica.calcular_media()

    def test_media_nNumeros_retornaMedia(self):
        # Arrange
        self.estadistica.numeros = [15.62, 15.9, 14.5]
        resultadoEsperado = 15.340

        # Do
        resultadoActual = self.estadistica.calcular_media()

        # Assert
        self.assertAlmostEqual(resultadoActual, resultadoEsperado, places=5)

    def test_media_nCasosNumeros_retornaMedia(self):
        # Arrange
        items = (
            {"Case": "Caso 01", "datos": [], "media": none, "desvstd": none},
            {"Case": "Caso 02", "datos": [3, 5], "media": 3.500, "desvstd": 1.414},
            {"Case": "Caso 03", "datos": [4, 6, 8], "media": 6, "desvstd": 2},
            {"Case": "Caso 04", "datos": [4, 6, 8, 12.5], "media": 7.625,
             "desvstd": 3.637},
            {"Case": "Caso 05", "datos": [3.5, 8, -4.2], "media": 2.433, "desvstd": 6.170},
            {"Case": "Caso 06", "datos": [0, 0, 0, 0], "media": 0,
             "desvstd": 0},
            {"Case": "Caso 07", "datos": [5, “4.5”], "media": 0,
             "desvstd": 0},
            {"Case": "Caso 08", "datos":[8, “a”], "media": 0,
            "desvstd": 0},
        )
        for item in items:
            with self.subTest(item["Case"]):
                self.estadistica.numeros = item["datos"]
            resultadoEsperado = item["media"]

            # Do
            resultadoActual = self.estadistica.calcular_media()

            # Assert
            self.assertAlmostEqual(resultadoActual, resultadoEsperado, places=3)