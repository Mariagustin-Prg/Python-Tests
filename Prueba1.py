import unittest

# Problema 1: Suma de Números Pares
def suma_pares(n):
    return sum(x for x in range(n + 1) if x % 2 == 0)

class TestSumaPares(unittest.TestCase):
    def test_suma_pares(self):
        self.assertEqual(suma_pares(10), 30)
        self.assertEqual(suma_pares(15), 56)
        self.assertEqual(suma_pares(5), 6)
        self.assertEqual(suma_pares(0), 0)

# Problema 2: Palíndromo
def es_palindromo(cadena):
    return cadena == cadena[::-1]

class TestEsPalindromo(unittest.TestCase):
    def test_es_palindromo(self):
        self.assertTrue(es_palindromo("radar"))
        self.assertFalse(es_palindromo("python"))
        self.assertTrue(es_palindromo("reconocer"))
        self.assertTrue(es_palindromo(""))

# Problema 3: Clase Punto
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro_punto):
        return ((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2) ** 0.5

class TestPunto(unittest.TestCase):
    def test_distancia(self):
        punto1 = Punto(0, 0)
        punto2 = Punto(3, 4)
        self.assertEqual(punto1.distancia(punto2), 5.0)

if __name__ == '__main__':
    unittest.main()
