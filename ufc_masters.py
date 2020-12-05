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

print(data2.keys())

print(data2.head())
print(data2.describe())

df = pd.DataFrame(data2)
print(df)

df = pd.DataFrame(data2.Winner)
print(df)

df = pd.DataFrame(data2.no_of_rounds) # Quantos rounds durou a maior luta?
print(df.head())

df = pd.DataFrame(data2.B_longest_win_streak) # Quem ganhou mais vezes seguidas? (Blue)
print(df.head())

df = pd.DataFrame(data2.R_longest_win_streak) # Quem ganhou mais vezes seguidas? (Red)
print(df.head())

df = pd.DataFrame(data2.B_current_lose_streak) # Quem perdeu mais vezes seguidas? (Blue)
print(df.head())

df = pd.DataFrame(data2.R_current_lose_streak) # Quem perdeu mais vezes seguidas? (Red)
print(df.head())
#######################################################

##############PLOT VENCEDORES POR GENERO###############
# print(data2.groupby("weight_class").mean())
# print(data2.groupby("gender").mean())
# print(data2.groupby(["weight_class", "gender"]).mean())

# vencedores_por_peso_genero = data2.groupby(["weight_class", "gender"]).mean()
# print(type(vencedores_por_peso_genero))

# vencedores_por_peso_genero["Winner"].plot.bar()
# plt.show()


# df["VENCEDOR"] = data2.Winner
# print(df.head(3))

# print(df.describe())

# #######################################################

# independentes = df.drop("VENCEDOR", axis = 1)
# dependente = df["VENCEDOR"]

# #Dividir o conjunto de dados entre treino e teste

# X_treino, X_teste, Y_treino, Y_teste = model_selection.train_test_split(independentes, dependente, test_size = 0.4, random_state = 1)
# print(X_treino.shape)
# print(X_teste.shape)
# print(Y_treino.shape)
# print(Y_teste.shape)

# model = linear_model.LinearRegression()
# model.fit(X_treino, Y_treino)

# Y_previsto = model.predict(X_teste)

# plt.scatter(Y_teste, Y_previsto)
# plt.xlabel("Vitórias")
# plt.ylabel("Vitórias Previstas")
# plt.title("Vitórias x Vitórias Previstas")
# plt.show()

# plt.scatter(model.predict(X_treino), model.predict(X_treino) - Y_treino, color = "green", s =10, label = "Treino")
# plt.scatter(model.predict(X_teste), model.predict(X_teste) - Y_teste, color = "red", s =10, label = "Teste")
# plt.show()

# print("\n------------------------------------------------\n")
# print(model.score(X_treino, Y_treino))
# print("Intercept:", model.intercept_)
# print("Coef:", model.coef_)

# print("\n------------------------------------------------\n")
# mse = metrics.mean_squared_error(Y_teste, model.predict(X_teste))
# print(mse)