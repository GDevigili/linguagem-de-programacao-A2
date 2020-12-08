import Conexao as con
import pandas as pd

class CovidAeroporto():
    """Constroi um método para responder cada pergunta feita."""
    
    def __init__(self):
        """
        Inicia a conexao com o banco de dados, importa os dados e encerra a conexao.

        Returns
        -------
        None.

        """
        self.conexao = con.Conexao()
        self.df = self.conexao.getCovidImpactDataFrame()
        self.conexao.fecharConexao()    
           
    def baselinesPorPais(self):
        """
        Responde a pergunta 'Em quais países o número de voos aumentou comparado com o período?'.

        Returns
        -------
        DataFrame
            DataFrame com colunas 'Country' e 'PercentOfBaseLine'.

        """
        return pd.DataFrame(self.df[["Country", "PercentOfBaseline"]].groupby("Country").mean()).sort_values(by = "PercentOfBaseline", ascending=False)
    
    def baselinePorCidade(self):
        """
        Responde as perguntas 'Em que cidades dos EUA o número de voos aumentou?' e 'Em que cidades dos EUA o número de voos diminuiu?'.

        Returns
        -------
        DataFrame
            DataFrame com colunas 'City' e 'PercentOfBaseLine'.

        """
        return pd.DataFrame(self.df[["City", "PercentOfBaseline"]].groupby("City").mean().sort_values(by=['PercentOfBaseline'], ascending=False))
    
    
    def maiorNumeroVoosPorDia(self):
        """
        Responde as perguntas 'Qual dia teve o maior número de voos internacionalmente?'.

        Returns
        -------
        aux_df : DataFrame
            DataFrame com colunas 'Date' e 'QtdVoos'.

        """
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["QtdVoos"]
        maiorNumeroVoos = max(aux_df["QtdVoos"])
        
        return aux_df[aux_df["QtdVoos"] == maiorNumeroVoos]
        # aux_df = pd.DataFrame(self.df["Date"].value_counts())
        # aux_df.columns = ["QtdVoos"]
        # return aux_df
        # return aux_df.sort_values(by = aux_df["QtdVoos"], ascending = True)
        # a linha acima estava retornando um key error
    
    def menorNumeroVoosPorDia(self):
        """
        Responde as perguntas 'Qual dia teve o menor número de voos internacionalmente?'.

        Returns
        -------
        aux_df : DataFrame
            DataFrame com colunas 'Date' e 'QtdVoos'.

        """
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["QtdVoos"]
        menorNumeroVoos = min(aux_df["QtdVoos"])
        
        return aux_df[aux_df["QtdVoos"] == menorNumeroVoos]

    def baselinePorDia(self):
        """
        Responde as perguntas 'Comparando o dia com mais voos com o mesmo dia da semana no período de baseline, o número de voos aumentou ou abaixou?' e 'Comparando o dia com menos voos com o mesmo dia da semana no período de baseline, o número de voos aumentou ou abaixou?'.

        Returns
        -------
        DataFrame
            DataFrame com colunas 'Date' e 'PercentOfBaseLine'.

        """
        return pd.DataFrame(self.df[["Date", "PercentOfBaseline"]].groupby("Date").mean().sort_values(by=['PercentOfBaseline'], ascending=False))

a = CovidAeroporto()

# Qual dia teve o maior número de voos internacionalmente?
print(a.maiorNumeroVoosPorDia())
# Qual dia teve o menor número de voos internacionalmente?
print(a.menorNumeroVoosPorDia())
# Comparando o dia com mais voos com o mesmo dia da semana no período de baselina, o número de voos aumentou ou abaixou?
if a.maiorNumeroVoosPorDia() >= a.baselinePorDia():
   print("O número de voos aumentou")
else: print("O número de voos diminuiu")    
# Comparando o dia com menos voos com o mesmo dia da semana no período de baselina, o número de voos aumentou ou abaixou?
if a.menorNumeroVoosPorDia() >= a.baselinePorDia():
   print("O número de voos aumentou")
else: print("O número de voos diminuiu")
# Em quais países o número de voos aumentou comparado com o período?
if a.baselinesPorPais() >= a.baselinePorDia():
    print(con.Country)
# Em que cidades dos EUA o número de voos aumentou?
if a.baselinePorCidade >= a.baselinePorDia():
   print(con.City)  
# Em que cidades dos EUA o número de voos diminuiu?
if a.baselinePorCidade <= a.baselinePorDia():
   print(con.City)