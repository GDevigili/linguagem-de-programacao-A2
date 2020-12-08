import UFCMaster as ufc
import unittest

# Acesso à classe do arquivo UFCMaster não está funcionando
# Arrumar respostas dos testes

class TesteModuloUFCMaster(unittest.TestCase):
    def test_vitoriasPorLado(self):
        self.assertEqual(ufc.vitoriasPorLado(), "Vermelho")
        
    def test_vitoriasPorLutador(self):
        self.assertEqual(ufc.vitoriasPorLutador(), ['Donald Cerrone'])
        
    def test_contagemCategoria(self):
        self.assertEqual(ufc.contagemCategoria(), "Lightweight")
    
    def test_vitoriasSeguidas(self):
        self.assertEqual(ufc.vitoriasSeguidas(), ['Anderson Silva'])
        
    def test_derrotasSeguidas(self):
        self.assertEqual(ufc.derrotasSeguidas(), ['BJ Penn'])
        
    def test_maiorLuta(self):
        self.assertEqual(ufc.maiorLuta(), 5)
        
    def test_menorLuta(self):
        self.assertEqual(ufc.menorLuta(), 4059)
        
    def test_ataquesSignificativos(self):
        self.assertEqual(ufc.ataquesSignificativos(), None)
        
    def test_idadeMaxima(self):
        self.assertEqual(ufc.idades(), "A idade é: 47 (Lado vermelho)")
        
    def test_void(self):
        self.assertEqual(ufc.Void(), 317)
        
    def test_decisao(self):
        self.assertEqual(ufc.Decisao(), None)
        
# c = TesteModuloUFCMaster()
# c.test_vitoriasPorLado()
# c.test_vitoriasPorLutador()
# c.test_contagemCategoria()
# c.test_vitoriasSeguidas()
# c.test_derrotasSeguidas()
# c.test_maiorLuta()
# c.test_menorLuta()
# c.test_ataquesSignificativos()
# c.test_idadeMaxima()
# c.test_void()
# c.test_decisao()
