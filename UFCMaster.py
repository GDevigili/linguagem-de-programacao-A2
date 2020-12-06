import Conexao as con
import pandas as pd

#FAZER CLASSE AQUI

class UFCMaster:
    # Cada função é referente à uma pergunta
    
    def __init__(self):
        self.conexao = con.Conexao()
        self.df = self.conexao.getUfcDataFrame()
        self.conexao.fecharConexao()    
    
    # Qual lado ganhou mais?
    def vitoriasPorLado(self):
        vitoriasAzul = self.df[self.df["Winner"] == "Blue"]["Winner"].value_counts().head(1)[0]
        vitoriasVermelhas = self.df[self.df["Winner"] == "Red"]["Winner"].value_counts().head(1)[0]
        
        if vitoriasVermelhas > vitoriasAzul:
            print("Lado vermelho ganhou mais, com um total de",vitoriasVermelhas," vitorias\n")
            return "Vermelho"
        elif vitoriasAzul > vitoriasVermelhas:
            print("Lado azul ganhou mais, com um total de",vitoriasAzul," vitorias\n")
            return "Azul"
        else:
            print("Empate no numero de vitorias: quantidade de vitorias de cada lado:",vitoriasAzul)
            return "Empate"
        
    # Quem ganhou mais lutas?
    def vitoriasPorLutador(self):
        vermelhos = self.df[self.df["Winner"] == "Red"]["R_fighter"]#.groupby(self.df['R_fighter']).count()
        
        azuis = self.df[self.df["Winner"] == "Blue"]["B_fighter"]#.groupby(self.df['B_fighter']).count()
        #a = reds["R_fighter"].groupby(self.df['R_fighter']).count()
        #print(vermelhos)
        #print(azuis)
        
        result = pd.concat([azuis,vermelhos], ignore_index=True)
        
        #self.df.pivot_table(index=['Values'], aggfunc='size')
        print(result)                      
                                     
        
    # Qual peso que tem mais integrantes?
    def contagemCategoria(self):
        
        grouped = self.df[['weight_class']].groupby(self.df['weight_class'])
        contGrupos = grouped.count()
        
        categoria = contGrupos[contGrupos.values == max(contGrupos.values)].index[0]
        print("A categoria de peso que mais tem integrantes é "+categoria)
        return categoria
        
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
    
u = UFCMaster()
#u.contagemCategoria()
u.vitoriasPorLutador()
#print(u.contagemCategoria())