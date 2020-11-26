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
