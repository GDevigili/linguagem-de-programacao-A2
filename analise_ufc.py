import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets, linear_model, metrics, model_selection
import seaborn as sns
import Conexao as con

c = con.Conexao()
data2 = c.getUfcDataFrame()

print(data2.keys())

print(data2.head())
print(data2.describe())

df = pd.DataFrame(data2)
print(df)

print("\n------------------------------------------------\n")
print("LADO VENCEDOR")
#df = pd.DataFrame(data2.Winner) 
print(data2[u'Winner'].value_counts())

print("\n------------------------------------------------\n")
print("NÚMERO DE ROUNDS POR PARTIDA")
#df = pd.DataFrame(data2.no_of_rounds) # Quantos rounds durou a maior luta?
print(data2[u'no_of_rounds'].value_counts())
print("Valor médio:")
print(data2[u'no_of_rounds'].mean())

print("\n------------------------------------------------\n")
print("MAIOR SÉRIE DE VITÓRIAS DO LADO AZUL")
df = pd.DataFrame(data2.B_longest_win_streak) 
print(df)
print("Valor médio:")
print(data2[u'B_longest_win_streak'].mean())

print("\n------------------------------------------------\n")
print("MAIOR SÉRIE DE VITÓRIAS DO LADO VERMELHO")
df = pd.DataFrame(data2.R_longest_win_streak) 
print(df)
print("Valor médio:")
print(data2[u'R_longest_win_streak'].mean())

print("\n------------------------------------------------\n")
print("SÉRIE DE VITÓRIAS ATUAL DO LADO AZUL")
df = pd.DataFrame(data2.B_current_win_streak) 
print(df)
print("Valor médio:")
print(data2[u'B_current_win_streak'].mean())

print("\n------------------------------------------------\n")
print("SÉRIE DE VITÓRIAS ATUAL DO LADO VERMELHO")
df = pd.DataFrame(data2.R_current_win_streak) 
print(df)
print("Valor médio:")
print(data2[u'R_current_win_streak'].mean())

print("\n------------------------------------------------\n")
print("SÉRIE DE DERROTAS ATUAL DO LADO AZUL")
df = pd.DataFrame(data2.B_current_lose_streak) 
print(df)
print("Valor médio:")
print(data2[u'B_current_lose_streak'].mean())

print("\n------------------------------------------------\n")
print("SÉRIE DE DERROTAS ATUAL DO LADO VERMELHO")
df = pd.DataFrame(data2.R_current_lose_streak) 
print(df)
print("Valor médio:")
print(data2[u'R_current_lose_streak'].mean())

print("\n------------------------------------------------\n")
print("PAÍSES")
print(data2[u'country'].value_counts())

print("\n------------------------------------------------\n")
print("TOTAL DE ROUNDS LUTADOS PELO LADO AZUL")
df = pd.DataFrame(data2.B_total_rounds_fought) 
print(df)
print("Valor médio:")
print(data2[u'B_total_rounds_fought'].mean())

print("\n------------------------------------------------\n")
print("TOTAL DE ROUNDS LUTADOS PELO LADO VERMELHO")
df = pd.DataFrame(data2.R_total_rounds_fought) 
print(df)
print("Valor médio:")
print(data2[u'R_total_rounds_fought'].mean())
#######################################################
print("\n------------------------------------------------\n")
print("PLOT NUMERO DE ROUNDS POR PESO/GENERO")
print(data2.groupby("weight_class").mean())
print(data2.groupby("gender").mean())
print(data2.groupby(["weight_class", "gender"]).mean())

rounds_por_peso_genero = data2.groupby(["weight_class", "gender"]).mean()
print(type(rounds_por_peso_genero))

rounds_por_peso_genero["no_of_rounds"].plot.bar()
plt.show()

#######################################################
print("\n------------------------------------------------\n")
print("PLOT NUMERO DE VITÓRIAS/DERROTAS POR ROUND (AZUL)")
print(data2.groupby("B_wins").mean())
print(data2.groupby("B_losses").mean())
print(data2.groupby(["B_wins", "B_losses"]).mean())

vitorias_derrotas_B = data2.groupby(["B_wins", "B_losses"]).mean()
print(type(vitorias_derrotas_B))

vitorias_derrotas_B["B_total_rounds_fought"].plot.bar()
plt.show()

# agrupamento1 = pd.cut(df["B_wins"], np.arange(0, 100, 5))
# agrupamento2 = pd.cut(df["B_losses"], np.arange(0, 100, 5))
# sobreviventes_por_idade = df.groupby(agrupamento1).mean()
# sobreviventes_por_idade["B_total_rounds_fought"].plot.bar()
# plt.show()

#######################################################
print("\n------------------------------------------------\n")
print("PLOT NUMERO DE VITÓRIAS/DERROTAS POR ROUND (VERMELHO)")
print(data2.groupby("R_wins").mean())
print(data2.groupby("R_losses").mean())
print(data2.groupby(["R_wins", "R_losses"]).mean())

vitorias_derrotas_R = data2.groupby(["R_wins", "R_losses"]).mean()
print(type(vitorias_derrotas_R))

vitorias_derrotas_R["R_total_rounds_fought"].plot.bar()
plt.show()

#######################################################
print("\n------------------------------------------------\n")
print("PREVISÃO DE ROUNDS")
df["NUMERO DE ROUNDS"] = data2.no_of_rounds
print(df)

print(df.describe())

independentes = df.drop("NUMERO DE ROUNDS", axis = 1)
dependente = df["NUMERO DE ROUNDS"]

#Dividir o conjunto de dados entre treino e teste

X_treino, X_teste, Y_treino, Y_teste = model_selection.train_test_split(independentes, dependente, test_size = 0.1, random_state = 1)
print(X_treino.shape)
print(X_teste.shape)
print(Y_treino.shape)
print(Y_teste.shape)

model = linear_model.LinearRegression()
model.fit(X_treino, Y_treino)

Y_previsto = model.predict(X_teste)

plt.scatter(Y_teste, Y_previsto)
plt.xlabel("Rounds")
plt.ylabel("Rounds Previstos")
plt.title("Rounds x Rounds Previstos")
plt.show()

plt.scatter(model.predict(X_treino), model.predict(X_treino) - Y_treino, color = "green", s =10, label = "Treino")
plt.scatter(model.predict(X_teste), model.predict(X_teste) - Y_teste, color = "red", s =10, label = "Teste")
plt.show()

print("\n------------------------------------------------\n")
print(model.score(X_treino, Y_treino))
print("Intercept:", model.intercept_)
print("Coef:", model.coef_)

print("\n------------------------------------------------\n")
mse = metrics.mean_squared_error(Y_teste, model.predict(X_teste))
print(mse)