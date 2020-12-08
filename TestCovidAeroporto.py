import CovidAeroporto as cov
import unittest

c = cov.CovidAeroporto()

class TesteModuloCovidAeroporto(unittest.TestCase):
    def test_baselinesPorPais(self):
        self.assertEqual(c.baselinesPorPais(), DataFrame...)
        
    def test_baselinePorCidade(self):
        self.assertEqual(c.baselinePorCidade(), DataFrame...)
        
    def test_maiorNumeroVoosPorDia(self):
        self.assertEqual(c.maiorNumeroVoosPorDia(), DataFrame...)
    
    def test_menorNumeroVoosPorDia(self):
        self.assertEqual(c.menorNumeroVoosPorDia(), DataFrame...)
        
    def test_baselinePorDia(self):
        self.assertEqual(c.baselinePorDia(), DataFrame...)
        
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
