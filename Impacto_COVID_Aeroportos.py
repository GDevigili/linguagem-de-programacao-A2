import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets, linear_model, metrics, model_selection

data1 = pd.read_csv("datasets/covid_impact_on_airport_traffic.csv", index_col=0)

#QUESTÕES IMPACTOS DO COVID NOS AEROPORTOS:

# Em quais países o número de voos aumentou comparado com o período de baselina?
# Em que cidades dos EUA o número de voos aumentou?
# Em que cidades dos EUA o número de voos diminuiu?
# Qual dia teve o maior número de voos internacionalmente?
# Qual dia teve o menor número de voos internacionalmente?
# Comparando o dia com mais voos com o mesmo dia da semana no período de baselina, o número de voos aumentou ou abaixou?
# Comparando o dia com menos voos com o mesmo dia da semana no período de baselina, o número de voos aumentou ou abaixou?
# Qual estado americano tem o maior centroide de aeroportos?


print(data1.keys())

df1 = pd.DataFrame(data1.PercentOfBaseline)
print(df1.head(3))