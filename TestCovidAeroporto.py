import CovidAeroporto as cov
import unittest

c = cov.CovidAeroporto()

class TesteModuloCovidAeroporto(unittest.TestCase):
        
    def test_maiorNumeroVoosPorDia(self):
        self.assertIsNotNone(c.maiorNumeroVoosPorDia())
    
    def test_menorNumeroVoosPorDia(self):
        self.assertIsNotNone(c.menorNumeroVoosPorDia())
        
    def test_maiorBaselinePorDia(self):
        self.assertIsNotNone(c.maiorBaselinePorDia())
        
    def test_menorBaselinePorDia(self):
        self.assertIsNotNone(c.menorBaselinePorDia())     
     
    def test_maiorBaselinePorCidade(self):
        self.assertIsNotNone(c.maiorBaselinePorCidade())
        
    def test_maiorBaselinePorEstado(self):
        self.assertIsNotNone(c.maiorBaselinePorEstado())  
     
    def test_maiorBaselinePorPais(self):
        self.assertIsNotNone(c.maiorBaselinePorPais())     
        
    def test_menorBaselinePorCidade(self):
       self.assertIsNotNone(c.menorBaselinePorCidade())    
        
    def test_menorBaselinePorEstado(self):
        self.assertIsNotNone(c.menorBaselinePorEstado())
        
    def test_menorBaselinePorPais(self):
        self.assertIsNotNone(c.menorBaselinePorPais())    
        
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
