import Conexao as con
import pandas as pd

#FAZER CLASSE AQUI

class UFCMaster:
    """Constroi um método para responder cada pergunta feita."""
    
    def __init__(self):
        """Inicia a conexao com o banco de dados, importa os dados e encerra a conexao."""
        self.conexao = con.Conexao()
        self.df = self.conexao.getUfcDataFrame()
        self.conexao.fecharConexao()    
    
    def vitoriasPorLado(self):
        """Responde a pergunta 'Qual lado ganhou mais?'"""
        vitoriasAzul = self.df[self.df["Winner"] == "Blue"]["Winner"].value_counts().head(1)[0]
        vitoriasVermelhas = self.df[self.df["Winner"] == "Red"]["Winner"].value_counts().head(1)[0]
        
        if (vitoriasVermelhas > vitoriasAzul):
            return "Vermelho"
        elif (vitoriasAzul > vitoriasVermelhas):
            return "Azul"
        else:
            return "Empate"
        
    def vitoriasPorLutador(self):
        """Responde a pergunta 'Quem ganhou mais lutas?'"""
        vermelhos = self.df[self.df["Winner"] == "Red"]["R_fighter"]
        
        azuis = self.df[self.df["Winner"] == "Blue"]["B_fighter"]
        winners = pd.concat([azuis,vermelhos], ignore_index=True)
        
        return winners.value_counts()[:1].index.tolist()[0]
     
    def contagemCategoria(self):
        """Responde a pergunta 'Qual peso que tem mais integrantes?'"""
        
        grouped = self.df[['weight_class']].groupby(self.df['weight_class'])
        contGrupos = grouped.count()
        
        categoria = contGrupos[contGrupos.values == max(contGrupos.values)].index[0]
        print("A categoria de peso que mais tem integrantes é "+categoria)
        return categoria
        
    def vitoriasSeguidas(self):
        """Responde a pergunta 'Quem ganhou mais vezes seguidas?'"""
        maximoVitoriasSeguidasB = max(self.df["B_longest_win_streak"])
        maximoVitoriasSeguidasR = max(self.df["R_longest_win_streak"])
        
        
        if (maximoVitoriasSeguidasB > maximoVitoriasSeguidasR):
            return self.df[self.df["B_longest_win_streak"] == maximoVitoriasSeguidasB]["B_fighter"].values
        elif (maximoVitoriasSeguidasR > maximoVitoriasSeguidasB):
            return self.df[self.df["R_longest_win_streak"] == maximoVitoriasSeguidasR]["R_fighter"].values
        else:
            r = self.df[self.df["R_longest_win_streak"] == maximoVitoriasSeguidasR]["R_fighter"].values
            b = self.df[self.df["B_longest_win_streak"] == maximoVitoriasSeguidasR]["B_fighter"].values
            losers = pd.concat([r,b], ignore_index=True)
            return losers.value_counts()[:1].index.tolist()[0]
    
    def derrotasSeguidas(self):
        """Responde a pergunta 'Quem perdeu mais vezes seguidas?'"""
        maximoDerrotasSeguidasB = max(self.df["B_current_lose_streak"])
        maximoDerrotasSeguidasR = max(self.df["R_current_lose_streak"])
        
        
        if (maximoDerrotasSeguidasB > maximoDerrotasSeguidasR):
            return self.df[self.df["B_current_lose_streak"] == maximoDerrotasSeguidasB]["B_fighter"].values
        elif (maximoDerrotasSeguidasR > maximoDerrotasSeguidasB):
            return self.df[self.df["R_current_lose_streak"] == maximoDerrotasSeguidasR]["R_fighter"].values
        else:
            r = self.df[self.df["R_current_lose_streak"] == maximoDerrotasSeguidasR]["R_fighter"].values
            b = self.df[self.df["B_current_lose_streak"] == maximoDerrotasSeguidasB]["B_fighter"].values
            losers = pd.concat([r,b], ignore_index=True)
            return losers.value_counts()[:1].index.tolist()[0]
        
    def maiorLuta(self):
        """Responde a pergunta 'Quantos rounds durou a maior luta?'"""
        return max(self.df["no_of_rounds"])
        
    def menorLuta(self):
        """Responde a pergunta 'Quais partidas duraram menos?'"""
        minimo = min(self.df["no_of_rounds"])
        return len(self.df[self.df["no_of_rounds"] == minimo])
    
