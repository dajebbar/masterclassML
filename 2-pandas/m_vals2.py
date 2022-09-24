import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

fp = 'https://bit.ly/missing-values'
fp2 = 'https://bit.ly/missing-values-toy'

df = pd.read_csv(fp)
# print(df.tail())

# print(df.isna().sum())
# print(df.color.value_counts(dropna=False))

df2 = pd.read_csv(fp2)
print(df2.head())
print(df2.isna().sum())
print(df2.isna().sum().sum())
print(df2['Colonne Importante'].value_counts(dropna=False))
