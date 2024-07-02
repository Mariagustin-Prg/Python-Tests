import unittest

# Implementa la función que calcula el factorial de un numero.

def factorial(numero):
    if not isinstance(numero, int):
        return None
    else:  
        if numero >= 1:
            factorial_n = numero
            pass
        elif numero == 0:
            return 1
    
        else: 
            return None
        
        while numero > 1:
            numero -= 1
            factorial_n = factorial_n * numero
        
        return factorial_n
    

class TestFactorial(unittest.TestCase):
    def test__factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(1.3), None)
        self.assertEqual(factorial('1'), None)

# Implementa la función que verifica si un número es primo.
def es_primo(sup_primo):
    list_divisores = [n for n in range(1, sup_primo + 1) if sup_primo % n == 0]
    if len(list_divisores) == 2:
        return True
    else:
        return False
    
class Test__Es_Primo_(unittest.TestCase):
    def test__es_primo(self):
        self.assertTrue(es_primo(2))
        self.assertFalse(es_primo(4))
        self.assertTrue(es_primo(17))
        self.assertFalse(es_primo(1000))

# Implementa la función que toma dos listas y devuelve una nueva lista
# que contiene los elementos comunes entre las dos listas, sin duplicados.
def lista_comun(lista_1, lista_2):
    return [i for i in lista_1 if i in lista_2]

class Test__Lista_Comun(unittest.TestCase):
    def test_lista_comun(self):
        self.assertEqual(lista_comun([1, 2, 4, 5], [2, 5]), [2, 5])
        self.assertEqual(lista_comun([7, 10, 11, 13], [7]), [7])
        self.assertEqual(lista_comun([], [3, 5, 6]), [])


if __name__ == '__main__':
    unittest.main()