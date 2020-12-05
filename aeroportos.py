import conexao as con
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets, linear_model, metrics, model_selection

#FAZER CLASSE AQUI

class CovidAeroporto():
    
    def __init__(self):
        self.conexao = con.Conexao()
        self.df = self.conexao.getCovidImpactDataFrame()
        self.conexao.fecharConexao()    
    
    # #QUESTÕES IMPACTOS DO COVID NOS AEROPORTOS:
    
    # # Em quais países o número de voos aumentou comparado com o período de baseline?
    def voosPorBaseline(self):
        pass
    
    # # Em que cidades dos EUA o número de voos aumentou?
    # # Em que cidades dos EUA o número de voos diminuiu?
    def voosPorCidade(self):
        pass    #podemos inserir um argumento opcional da ordenação que os dados vão vir
    
    # # Qual dia teve o maior número de voos internacionalmente?
    # # Qual dia teve o menor número de voos internacionalmente?
    def voosPorDia(self):
        pass    #podemos inserir um argumento opcional da ordenação que os dados vão vir
    
    # # Comparando o dia com mais voos com o mesmo dia da semana no período de baseline, o número de voos aumentou ou abaixou?
    # # Comparando o dia com menos voos com o mesmo dia da semana no período de baseline, o número de voos aumentou ou abaixou?
    def voosPorDiaSemana(self):
        pass
    
    # # Qual estado americano tem o maior centroide de aeroportos?
    def centroidePorEstado(self):
        pass
    

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