import unittest

# Implementa la función que verifica si un número es un número triangular.
# Un número triangular es aquel que puede representarse como la suma de los
# primeros N números naturales, por ejemplo, 1, 3, 6, 10 son números triangulares.
def es_numero_triangular(n):
    if not isinstance(n, int):
        return None
    
    elif n == 1:
        return True
    
    else:
        n_triangular = 0
        sum_n = 0
        while n_triangular < n:
            sum_n += 1
            n_triangular = n_triangular + sum_n
        
        return n_triangular == n
    
class TestNumeroTriangular(unittest.TestCase):
    def test__es_numero_triangular(self):
        self.assertTrue(es_numero_triangular(1))
        self.assertTrue(es_numero_triangular(3))
        self.assertTrue(es_numero_triangular(6))
        self.assertTrue(es_numero_triangular(10))
        self.assertFalse(es_numero_triangular(4))
        self.assertFalse(es_numero_triangular(8))

# Implementa la función que calcula la suma de los 
# cuadrados de los primeros N números naturales.

def suma_de_cuadrados(n_2):
    return sum([x**2 for x in range(1, n_2 + 1)])

class Test_Numero_Cuadrado(unittest.TestCase):
    def test_numero_cuadrado(self):
        self.assertEqual(suma_de_cuadrados(1), 1)
        self.assertEqual(suma_de_cuadrados(2), 5)
        self.assertEqual(suma_de_cuadrados(4), 30)

# Implementa la función que convierte una temperatura de grados Celsius a Fahrenheit.
# La fórmula de conversión es: Fahrenheit = (Celsius * 9/5) + 32

def conversor_celsius_fahrenheit(g_celsius):
    return round(g_celsius * (9 / 5) + 32, 1)

class Test_Fahrenheit(unittest.TestCase):
    def test_fahrenheit(self):
            self.assertEqual(conversor_celsius_fahrenheit(0), 32.0)
            self.assertEqual(conversor_celsius_fahrenheit(100), 212.0)
            self.assertEqual(conversor_celsius_fahrenheit(-40), -40.0)
            self.assertEqual(conversor_celsius_fahrenheit(37), 98.6)

if __name__ == '__main__':
    unittest.main()