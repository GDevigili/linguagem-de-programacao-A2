import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets, linear_model, metrics, model_selection

data1 = pd.read_csv("datasets/covid_impact_on_airport_traffic.csv", index_col=0)
data2 = pd.read_csv("datasets/ufc-master.csv", index_col=0)

#