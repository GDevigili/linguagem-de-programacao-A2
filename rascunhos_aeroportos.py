import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets, linear_model, metrics, model_selection

data1 = pd.read_csv("datasets/covid_impact_on_airport_traffic.csv", index_col=0)

print(data1.keys())

print(data1.head())
print(data1.describe())

df = pd.DataFrame(data1)
print(df)

print("\n------------------------------------------------\n")
print("NOME DOS AEROPORTOS")
df = pd.DataFrame(data1.AirportName) 
print(df)

print("\n------------------------------------------------\n")
print("PORCENTAGEM DE BASELINE")
df = pd.DataFrame(data1.PercentOfBaseline) # Baseline
print(df)

print("\n------------------------------------------------\n")
print("CENTROIDE")
print(data1[u'Centroid'].value_counts())
# df = pd.DataFrame(data1.Centroid) # Centroide
# print(df)

print("\n------------------------------------------------\n")
print("GEOGRAFIA")
print(data1[u'Geography'].value_counts())
# df = pd.DataFrame(data1.Geography) # Geografia
# print(df)

print("\n------------------------------------------------\n")
print("CIDADES")
print(data1[u'City'].value_counts())

print("\n------------------------------------------------\n")
print("ESTADOS")
print(data1[u'State'].value_counts())

print("\n------------------------------------------------\n")
print("PAÍSES")
print(data1[u'Country'].value_counts())

#######################################################

##############PLOT BASELINE POR CIDADE/PAIS###############
print(data1.groupby("City").mean())
print(data1.groupby("Country").mean())
print(data1.groupby(["City", "Country"]).mean())

baseline_cidade_paises = data1.groupby(["City", "Country"]).mean()
print(type(baseline_cidade_paises))

baseline_cidade_paises["PercentOfBaseline"].plot.bar()
plt.show()

#######################################################

df["NUMERO DE VOOS"] = data1.PercentOfBaseline
print(df.head(3))

print(df.describe())

independentes = df.drop("NUMERO DE VOOS", axis = 1)
dependente = df["NUMERO DE VOOS"]

#Dividir o conjunto de dados entre treino e teste

X_treino, X_teste, Y_treino, Y_teste = model_selection.train_test_split(independentes, dependente, test_size = 0.4, random_state = 1)
print(X_treino.shape)
print(X_teste.shape)
print(Y_treino.shape)
print(Y_teste.shape)

model = linear_model.LinearRegression()
model.fit(X_treino, Y_treino)

Y_previsto = model.predict(X_teste)

plt.scatter(Y_teste, Y_previsto)
plt.xlabel("Voos")
plt.ylabel("Voos Previstos")
plt.title("Voos x Voos Previstos")
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