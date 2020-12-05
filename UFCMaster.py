import conexao as con

#FAZER CLASSE AQUI

class UFCMaster:
    # Cada função é referente à uma pergunta
    
    def __init__(self):
        self.conexao = con.Conexao()
        self.df = self.conexao.getUfcDataFrame()
        self.conexao.fecharConexao()    
    
    # Qual lado ganhou mais?
    def vitoriasPorLado(self):
        pass
        
    # Quem ganhou mais lutas?
    def vitoriasPorLutador(self):
        pass
        
    # Qual peso que tem mais integrantes?
    def contagemCategoria(self):
        pass
    
    # Quem ganhou mais vezes seguidas?
    def vitoriasSeguidas(self):
        pass    
    
    # Quem perdeu mais vezes seguidas?
    def derrotasSeguidas(self):
        pass
        
    # Quantos rounds durou a maior luta?    
    def maiorLuta():
        pass
    
    # Quais partidas duraram menos?
    def menorLuta():
        pass
        
    def ordenar(self):
        pass #
    