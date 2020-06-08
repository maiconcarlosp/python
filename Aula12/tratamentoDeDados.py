import numpy as np
import pandas as pd
import pylab as pl
import matplotlib.pyplot as plt #estrutura de gráficos do matlab
import sklearn

df = pd.read_csv('Aula12/FuelConsumption.csv')

# print(df.dtypes)
# print(df.head(5))
# print(df.tail(5))
# print(df.columns)

# print(df.loc[9])
# print (df[9:10])
# df = df[1:] #remove primeira linha do csv

# print(df.index)
# print(list(df.columns)) #cria uma lista com as colunas

# print(df [(df["MAKE"] == "VOLVO") & (df["FUELCONSUMPTION_COMB_MPG"] > 25)])

# newdf = df[['MAKE', 'FUELCONSUMPTION_COMB_MPG']]
# print(newdf.head())

print(df.describe())

# ndf = df[ df["MAKE"] == "VOLVO"]
# ndf.to_csv('Aula12/volvo.csv')
# print(ndf.head())
