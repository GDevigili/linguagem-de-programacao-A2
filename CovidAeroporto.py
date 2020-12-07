import Conexao as con
import pandas as pd
from datetime import datetime

class CovidAeroporto():
    # Cada função é referente à uma pergunta
    
    def __init__(self):
        self.conexao = con.Conexao()
        self.df = self.conexao.getCovidImpactDataFrame()
        self.conexao.fecharConexao()    
        
    # # Em quais países o número de voos aumentou comparado com o período?    
    def baselinesPorPais(self):
        return pd.DataFrame(self.df[["Country", "PercentOfBaseline"]].groupby("Country").mean())
    
    # # Em que cidades dos EUA o número de voos aumentou?  
    # # Em que cidades dos EUA o número de voos diminuiu?
    def baselinePorCidade(self):
        return pd.DataFrame(self.df[["City", "PercentOfBaseline"]].groupby("City").mean())
    
    # # Qual dia teve o maior número de voos internacionalmente?
    # # Qual dia teve o menor número de voos internacionalmente?
    def numeroVoosPorDia(self):
        aux_df = pd.DataFrame(self.df["Date"].value_counts())
        aux_df.columns = ["QtdVoos"]
        return aux_df
        # return aux_df.sort_values(by = aux_df["QtdVoos"], ascending = True)
        # a linha acima estava retornando um key error
    
    # # Comparando o dia com mais voos com o mesmo dia da semana no período de baseline, o número de voos aumentou ou abaixou?
    # # Comparando o dia com menos voos com o mesmo dia da semana no período de baseline, o número de voos aumentou ou abaixou?
    def baselinePorDia(self):
        return pd.DataFrame(self.df[["Date", "PercentOfBaseline"]].groupby("Date").mean())
    
ca = CovidAeroporto()
print(ca.baselinePorCidade())
print("---------------------------------")
print(ca.baselinesPorPais())
print("---------------------------------")
print(ca.numeroVoosPorDia())
print("---------------------------------")
print(ca.baselinePorDia())
    
# -----------Já tava aqui antes

# print(data1.keys())

# print(data1.head())
# print(data1.describe())

# df = pd.DataFrame(data1)
# print(df)

# ##############PLOT COMPARACAO DE VOOS POR AEROPORTO###############
# print(data1.groupby("Date").mean())
# print(data1.groupby("AirportName").mean())
# print(data1.groupby(["Date", "AirportName"]).mean())

# viagens_por_aeroporto = data1.groupby(["Date", "AirportName"]).mean()
# print(type(viagens_por_aeroporto))

# viagens_por_aeroporto["PercentOfBaseline"].plot.bar()
# plt.show()
