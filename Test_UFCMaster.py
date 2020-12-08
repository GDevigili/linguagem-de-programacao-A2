import UFCMaster as ufc
import unittest

# Acesso à classe do arquivo UFCMaster não está funcionando
# Arrumar respostas dos testes

c = ufc.UFCMaster()

class TesteModuloUFCMaster(unittest.TestCase):
    def test_vitoriasPorLado(self):
        self.assertEqual(c.vitoriasPorLado(), "Vermelho")
        
    def test_vitoriasPorLutador(self):
        self.assertEqual(c.vitoriasPorLutador(), ['Donald Cerrone'])
        
    def test_contagemCategoria(self):
        self.assertEqual(c.contagemCategoria(), "Lightweight")
    
    def test_vitoriasSeguidas(self):
        self.assertEqual(c.vitoriasSeguidas(), ['Anderson Silva'])
        
    def test_derrotasSeguidas(self):
        self.assertEqual(c.derrotasSeguidas(), ['BJ Penn'])
        
    def test_maiorLuta(self):
        self.assertEqual(c.maiorLuta(), 5)
        
    def test_menorLuta(self):
        self.assertEqual(c.menorLuta(), 4059)
        
    def test_ataquesSignificativos(self):
        self.assertEqual(c.ataquesSignificativos(), None)
        
    def test_idadeMaxima(self):
        self.assertEqual(c.idadeMaxima(), "A idade é: 47 (Lado vermelho)")
        
    def test_void(self):
        self.assertEqual(c.void(), 317)
        
    def test_decisao(self):
        self.assertEqual(c.decisao(), "Donald Cerrone")
        
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
        
# x = TesteModuloUFCMaster()
# x.test_vitoriasPorLado()
# x.test_vitoriasPorLutador()
# x.test_contagemCategoria()
# x.test_vitoriasSeguidas()
# x.test_derrotasSeguidas()
# x.test_maiorLuta()
# x.test_menorLuta()
# x.test_ataquesSignificativos()
# x.test_idades()
# x.test_Void()
# x.test_Decisao()



