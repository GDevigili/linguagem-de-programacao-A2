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
            return "Vermelho"
        elif vitoriasAzul > vitoriasVermelhas:
            return "Azul"
        else:
            return "Empate"
        
    # Quem ganhou mais lutas?
    def vitoriasPorLutador(self):
        vermelhos = self.df[self.df["Winner"] == "Red"]["R_fighter"]
        
        azuis = self.df[self.df["Winner"] == "Blue"]["B_fighter"]
        winners = pd.concat([azuis,vermelhos], ignore_index=True)
        
        return winners.value_counts()[:1].index.tolist()[0]
     
    # Qual peso que tem mais integrantes?
    def contagemCategoria(self):
        
        grouped = self.df[['weight_class']].groupby(self.df['weight_class'])
        contGrupos = grouped.count()
        
        categoria = contGrupos[contGrupos.values == max(contGrupos.values)].index[0]
        print("A categoria de peso que mais tem integrantes é "+categoria)
        return categoria
        
    # Quem ganhou mais vezes seguidas?
    def vitoriasSeguidas(self):
        maximoVitoriasSeguidasB = max(self.df["B_longest_win_streak"])
        maximoVitoriasSeguidasR = max(self.df["R_longest_win_streak"])
        
        
        if(maximoVitoriasSeguidasB > maximoVitoriasSeguidasR):
            return self.df[self.df["B_longest_win_streak"] == maximoVitoriasSeguidasB]["B_fighter"].values
        elif (maximoVitoriasSeguidasR > maximoVitoriasSeguidasB):
            return self.df[self.df["R_longest_win_streak"] == maximoVitoriasSeguidasR]["R_fighter"].values
        else:
            r = self.df[self.df["R_longest_win_streak"] == maximoVitoriasSeguidasR]["R_fighter"].values
            b = self.df[self.df["B_longest_win_streak"] == maximoVitoriasSeguidasR]["B_fighter"].values
            losers = pd.concat([r,b], ignore_index=True)
            return losers.value_counts()[:1].index.tolist()[0]
    
    # Quem perdeu mais vezes seguidas?
    def derrotasSeguidas(self):
        maximoDerrotasSeguidasB = max(self.df["B_current_lose_streak"])
        maximoDerrotasSeguidasR = max(self.df["R_current_lose_streak"])
        
        
        if(maximoDerrotasSeguidasB > maximoDerrotasSeguidasR):
            return self.df[self.df["B_current_lose_streak"] == maximoDerrotasSeguidasB]["B_fighter"].values
        elif (maximoDerrotasSeguidasR > maximoDerrotasSeguidasB):
            return self.df[self.df["R_current_lose_streak"] == maximoDerrotasSeguidasR]["R_fighter"].values
        else:
            r = self.df[self.df["R_current_lose_streak"] == maximoDerrotasSeguidasR]["R_fighter"].values
            b = self.df[self.df["B_current_lose_streak"] == maximoDerrotasSeguidasB]["B_fighter"].values
            losers = pd.concat([r,b], ignore_index=True)
            return losers.value_counts()[:1].index.tolist()[0]
        
    # Quantos rounds durou a maior luta?    
    def maiorLuta(self):
        return max(self.df["no_of_rounds"])
        
    
    # Quais partidas duraram menos?
    def menorLuta(self):
        minimo = min(self.df["no_of_rounds"])
        return len(self.df[self.df["no_of_rounds"] == minimo])
    