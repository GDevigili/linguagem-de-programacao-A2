import CovidAeroporto as cov
import unittest

# Acesso à classe do arquivo CovidAeroporto não está funcionando
# Arrumar respostas dos testes

class TesteModuloCovidAeroporto(unittest.TestCase):
    def test_baselinesPorPais(self):
        self.assertEqual(cov.baselinesPorPais(), DataFrame...)
        
    def test_baselinePorCidade(self):
        self.assertEqual(cov.baselinePorCidade(), DataFrame...)
        
    def test_maiorNumeroVoosPorDia(self):
        self.assertEqual(cov.maiorNumeroVoosPorDia(), DataFrame...)
    
    def test_menorNumeroVoosPorDia(self):
        self.assertEqual(cov.menorNumeroVoosPorDia(), DataFrame...)
        
    def test_baselinePorDia(self):
        self.assertEqual(cov.baselinePorDia(), DataFrame...)
