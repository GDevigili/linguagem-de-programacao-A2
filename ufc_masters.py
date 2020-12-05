import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets, linear_model, metrics, model_selection

data2 = pd.read_csv("datasets/ufc-master.csv", index_col=0)

#QUESTÕES UFC:

# Qual lado ganhou mais?
# Quem ganhou mais lutas?
# Quais partidas duraram menos?
# Qual peso que tem mais integrantes?
# Quem ganhou mais vezes seguidas?
# Quem perdeu mais vezes seguidas?
# Quantos rounds durou a maior luta?

# print(data2.keys())
# maior_luta = data2.groupby(["no_of_rounds"]).max()

print(data2.head())
print(data2.describe())

df = pd.DataFrame(data2.no_of_rounds) # Quantos rounds durou a maior luta?
print(df.head(1))

df = pd.DataFrame(data2.B_longest_win_streak) # Quem ganhou mais vezes seguidas? (Blue)
print(df.head(1))

df = pd.DataFrame(data2.R_longest_win_streak) # Quem ganhou mais vezes seguidas? (Red)
print(df.head(1))

df = pd.DataFrame(data2.B_current_lose_streak) # Quem perdeu mais vezes seguidas? (Blue)
print(df.head(1))

df = pd.DataFrame(data2.R_current_lose_streak) # Quem perdeu mais vezes seguidas? (Red)
print(df.head(1))