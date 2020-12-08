import UFCMaster as ufc
import unittest

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
        
    def test_idadeMaxima(self):
        self.assertEqual(c.idadeMaxima(), "A idade é: 47 (Lado vermelho)")
        
    def test_void(self):
        self.assertEqual(c.void(), 317)
        
    def test_decisao(self):
        self.assertEqual(c.decisao(), ['Rafael Dos Anjos'])
        
    def test_diferenca(self):
        self.assertEqual(c.diferenca(), 765)
        
        
        
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
