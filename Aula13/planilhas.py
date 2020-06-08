import numpy as np
import pandas as pd
import pylab as pl
import matplotlib.pyplot as plt
import sklearn

df = pd.read_csv('Aula12/FuelConsumption.csv')

# histograma = df[ ['CYLINDERS', 'ENGINESIZE', 'CO2EMISSIONS', 'FUELCONSUMPTION_COMB']]
# histograma.hist()
# plt.show()

# plt.scatter(df['CYLINDERS'])
# igual
plt.scatter(df.CYLINDERS, df.CO2EMISSIONS)
plt.xlabel('Cilindros')
plt.ylabel('CO2')
plt.show()
