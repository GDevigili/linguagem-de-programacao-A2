import CovidAeroporto as cov
import unittest

c = cov.CovidAeroporto()

class TesteModuloCovidAeroporto(unittest.TestCase):
        
    def test_maiorNumeroVoosPorDia(self):
        self.assertEqual(c.maiorNumeroVoosPorDia(), DataFrame...)
    
    def test_menorNumeroVoosPorDia(self):
        self.assertEqual(c.menorNumeroVoosPorDia(), DataFrame...)
        
    def test_maiorBaselinePorDia(self):
        self.assertEqual(c.maiorBaselinePorDia(), DataFrame...)
     
    def test_menorBaselinePorCidade(self):
        self.assertEqual(c.menorBaselinePorCidade(), DataFrame...)     
     
    def test_maiorBaselinePorEstado(self):
        self.assertEqual(c.maiorBaselinePorEstado(), DataFrame...)     
     
    def test_maiorBaselinePorPais(self):
        self.assertEqual(c.maiorBaselinePorPais(), DataFrame...)     
        
    def test_menorBaselinePorCidade(self):
        self.assertEqual(c.menorBaselinePorCidade(), DataFrame...)    
        
    def test_menorBaselinePorEstado(self):
        self.assertEqual(c.menorBaselinePorEstado(), DataFrame...)
        
    def test_menorBaselinePorPais(self):
        self.assertEqual(c.menorBaselinePorPais(), DataFrame...)    
        
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
