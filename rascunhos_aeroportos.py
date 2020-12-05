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

df = pd.DataFrame(data1.AirportName) # Nome dos aeroportos
print(df.head())

df = pd.DataFrame(data1.PercentOfBaseline) # Baseline
print(df.head())

df = pd.DataFrame(data1.Centroid) # Centroide
print(df.head())

df = pd.DataFrame(data1.Geography) # Geografia
print(df.head())

df = pd.DataFrame(data1.City) # Cidade
print(df.head())

df = pd.DataFrame(data1.State) # Estado
print(df.head())

df = pd.DataFrame(data1.Country) # Pais
print(df.head())
