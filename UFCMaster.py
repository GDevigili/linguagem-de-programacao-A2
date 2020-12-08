import Conexao as con
import pandas as pd

#FAZER CLASSE AQUI

class UFCMaster:
    """Constroi um método para responder cada pergunta feita."""
    
    def __init__(self):
        """
        Inicia a conexao com o banco de dados, importa os dados e encerra a conexao.

        Returns
        -------
        None.

        """
        self.conexao = con.Conexao()
        self.df = self.conexao.getUfcDataFrame()
        self.conexao.fecharConexao()    
    
    def vitoriasPorLado(self):
        """
        Responde a pergunta 'Qual lado ganhou mais?'.

        Returns
        -------
        str
            Nome do lado com mais vitórias.

        """
        vitoriasAzul = self.df[self.df["Winner"] == "Blue"]["Winner"].value_counts().head(1)[0]
        vitoriasVermelhas = self.df[self.df["Winner"] == "Red"]["Winner"].value_counts().head(1)[0]
        
        if (vitoriasVermelhas > vitoriasAzul):
            return "Vermelho"
        elif (vitoriasAzul > vitoriasVermelhas):
            return "Azul"
        else:
            return "Empate"
        
    def vitoriasPorLutador(self):
        """
        Responde a pergunta 'Quem ganhou mais lutas?'.

        Returns
        -------
        str
            Nome do lutador com mais vitórias.

        """
        vermelhos = self.df[self.df["Winner"] == "Red"]["R_fighter"]
        
        azuis = self.df[self.df["Winner"] == "Blue"]["B_fighter"]
        winners = pd.concat([azuis,vermelhos], ignore_index=True)
        
        return winners.value_counts()[:1].index.tolist()[0]
     
    def contagemCategoria(self):
        """
        Responde a pergunta 'Qual peso que tem mais integrantes?'.

        Returns
        -------
        categoria : str
            Categoria de peso com mais integrantes.

        """
        
        grouped = self.df[['weight_class']].groupby(self.df['weight_class'])
        contGrupos = grouped.count()
        
        categoria = contGrupos[contGrupos.values == max(contGrupos.values)].index[0]
        print("A categoria de peso que mais tem integrantes é "+categoria)
        return categoria
        
    def vitoriasSeguidas(self):
        """
        Responde a pergunta 'Quem ganhou mais vezes seguidas?'.

        Returns
        -------
        str
            Nome do lutador com mais vitórias seguidas.

        """
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
        """
        Responde a pergunta 'Quem perdeu mais vezes seguidas?'.

        Returns
        -------
        str
            Nome do lutador com mais derrotas seguidas.

        """
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
        """
        Responde a pergunta 'Quantos rounds durou a maior luta?'.

        Returns
        -------
        int
            Quantidade de rounds da luta mais longa.

        """
        return max(self.df["no_of_rounds"])
        
    def menorLuta(self):
        """
        Responde a pergunta 'Quantas partidas duraram menos rounds?'.

        Returns
        -------
        int
            Numero de partidas mais curtas.

        """
        minimo = min(self.df["no_of_rounds"])
        return len(self.df[self.df["no_of_rounds"] == minimo])

    def ataquesSignificativos(self):
        # vermelhos = self.df[self.df["R_avg_SIG_STR_landed"] == "Red"]["R_avg_SIG_STR_landed"]
        # azuis = self.df[self.df["B_avg_SIG_STR_landed"] == "Blue"]["B_avg_SIG_STR_landed"]
        
        # #maximoAtaquesSignificativosB = max(self.df["B_avg_SIG_STR_landed"])
        # #maximoAtaquesSignificativosR = max(self.df["R_avg_SIG_STR_landed"])
       
        # aux_df = pd.DataFrame(self.df[azuis, vermelhos].value_counts())
        # return aux_df
        
        pass
        
    def idades(self):
        """
        Responde a pergunta 'Quantos anos tem o lutador mais velho?'.

        Returns
        -------
        str
            Idade do lutador mais velho.

        """
         idadeAzul =  max(self.df["B_age"])
         idadeVermelha = max(self.df["R_age"])
         if idadeAzul > idadeVermelha:
             return (f"A idade é: {idadeAzul} (Lado azul)")
         else:
             return (f"A idade é: {idadeVermelha} (Lado vermelho)")
         
    def Void(self):
        """
        Responde a pergunta 'Quantas lutas aconteceram em uma arena vazia?'.

        Returns
        -------
        int
            Numero de lutas ocorridas em arenas vazias.

        """
        enchimento = max(self.df["empty_arena"])
        return len(self.df[self.df["empty_arena"] == enchimento])
    
    def Decisao(self):
        pass
    